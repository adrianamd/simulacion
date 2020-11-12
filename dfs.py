import sys 
from event import Event 
from model import Model 
from simulation import Simulation 
import random

class AlgorithmDFS(Model):
    
    def init(self):
        self.visited = False
        self.father = self.id
        self.sin_visitar = self.neighbors[:]
        self.hijos=[]
        self.rechazos=0
        print ("Nodo ",self.id," inicio algoritmo")
                
    def receive(self, event): 
        nombre = event.name()
        if event.getName()=="Descubre":
            print ("SOY",self.id)
            if self.visited == False:
                self.visited = True 
                self.father = event.getSource()
            aux=event.getSource()
            print ("Recibo Descubre de",aux,"papá",self.father,"en el tiempo",self.clock)
            if aux != self.father: 
                if aux != self.id: 
                    self.sin_visitar.remove(aux)
            if len(self.sin_visitar)>0: 
                for i in range(len(self.neighbors)): 
                    if self.neighbors[i] != self.father: 
                        newevent = Event("AVISO",self.clock+1.0,self.neighbors[i],self.id)    
                        self.transmit(newevent)
                print ("envio AVISO a los nodos vecinos menos padre")

            if len(self.sin_visitar)>0: 
                aleat=random.randint(0, len(self.sin_visitar)-1) 
                newevent = Event("Descubre",self.clock+1.0,self.sin_visitar[aleat],self.id)
                del self.sin_visitar[aleat]       
                self.transmit(newevent)
            else: 
                if self.father != self.id: 
                    newevent = Event("Regresa", self.clock+1.0, self.father, self.id)
                    self.transmit(newevent) 
                    if self.hijos == []:
                        for i in range(len(self.neighbors)):
                            if self.neighbors[i] != self.father: 
                                newevent = Event("AVISO",self.clock+1.0,self.neighbors[i],self.id)
                                self.transmit(newevent)
                    print ("envio AVISO a los nodos vecinos menos padre")

        if event.getName()=="AVISO":
            print ("SOY",self.id,"RECIBO AVISO DE",event.getSource(),"en el tiempo",self.clock,)
            aux=event.getSource()
            self.sin_visitar.remove(aux)
            print ("Lista sin visitar",self.sin_visitar)

        if event.getName()=="REGRESA":
            print ("SOY",self.id,"Recibo Regresa de",event.getSource(),"En el tiempo",self.clock)
            self.hijos.append(event.getSource())
            print ("Mis hijos",self.hijos)
            if len(self.sin_visitar)>0: 
                aleat=random.randint(0, len(self.sin_visitar)-1)
                newevent = Event("Descubre",self.clock+1.0,self.sin_visitar[aleat],self.id)
                del self.sin_visitar[aleat]       
                self.transmit(newevent)
            else:
                if self.father != self.id:
                    newevent = Event("Regresa",self.clock+1.0,self.father,self.id)
                    self.transmit(newevent)
            if self.father == self.id:
                newevent = Event("Final",self.clock+1.0,self.father,self.id)
                self.transmit(newevent)
                
        if event.getName()=="FINAL":
            print ("Final del algoritmo")
# ----------------------------------------------------------------------------------------
# "main()"
# ----------------------------------------------------------------------------------------

# construye una instancia de la clase Simulation recibiendo como parametros el nombre del 
# archivo que codifica la lista de adyacencias de la grafica y el tiempo max. de simulacion
if len(sys.argv) != 2:
    print ("Please supply a file name")
    raise SystemExit(1)
experiment = Simulation(sys.argv[1], 500)  

# asocia un pareja proceso/modelo con cada nodo de la grafica
for i in range(1,len(experiment.graph)+1):
    m = AlgorithmDFS()
    experiment.setModel(m, i)

# inserta un evento semilla en la agenda y arranca
seed = Event("DESCUBRE", 0.0, 1,1)
experiment.init(seed)
experiment.run()

