# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:31:14 2020
@author: Adriana Molina Delgado 
PROGRAMA 1 - Fila M/M/3/B ligada a una fila M/M/2/B
"""
from math import log
import random 

vel_arribo = 3.0
total_clientes = 2000

ilam = 1/vel_arribo
mu1=1/5
mu2=1/4
mu3=1/6

mu4 = 1/4
mu5 = 1/3

a = [] #arribo primer buffer
a2 = [] #guardar las entradas para poder restarlas al final 
previo = 0.0

entradas = [] #clientes que entran al servidor 1
entradas2 = [] #clientes que entran al servidor 2
entradas3 = [] #clientes que entran al servidor 3 

entradas4 = [] #clientes que entran al servidor 4
entradas5 = [] #clientes que entran al servidor 5

b = [] #inicio de servicio primer buffer
b2 = [] #inicio de servicio del segundo  buffer

c = [] #fin de servicio primer buffer
c2 = [] # fin de servicio del segundo buffer
salida = 0.0
salida2 = 0.0

d =[] #tiempo en el sistema primer buffer
suma = 0.0 #suma de los tiempos en el sistema 


buffer2 = [] #para insertar todas las salidas de la primera parte

servidor1 = [] #clientes que salen del servidor 1 
servidor2 = [] #clientes que salen del servidor 2
servidor3 = [] #clientes que salen del servidor 3

servidor4 = [] #clientes que salen del servidor 4
servidor5 = [] #clientes que salen del servidor 5

cont = 3 #contador de clientes atendidos en la primera parte
cont_buffer1 = 1987 #limite del primer buffer

cont2 = 2 #contador de clientes atendidos en la segunda parte
cont_buffer2 = 1885 #limite del segundo buffer

rechazadosb1 = 0 #rechzados del buffer 1
rechazadosb2 = 0 #rechazados del buffer 2 

print("------- INICIO DE SISTEMA ------\n")
for i in range(total_clientes):
    indice = i%2
    inter = -1*ilam*log(random.random())
    a.insert(indice, previo+inter)
    previo = a[indice]
    a2.append(previo)
    if (i==0):
        servidor1.append(previo) #agrego mi primer cliente al servidor 1
        b.insert(indice, max(salida,a[indice]))
        serv = -1*mu1*log(random.random())
        c.insert(indice, b[indice]+serv)
        salida = c[indice]
        buffer2.append(salida)
       
                
    elif (i==1):
        servidor2.append(previo) #agrego mi segundo cliente al servidor 2 
        b.insert(indice, max(salida,a[indice]))
        serv = -1*mu2*log(random.random())
        c.insert(indice, b[indice]+serv)
        salida = c[indice]
        buffer2.append(salida)
        
    elif (i==2):
        servidor3.append(previo)
        b.insert(indice, max(salida,a[indice]))
        serv = -1*mu3*log(random.random())
        c.insert(indice, b[indice]+serv)
        salida = c[indice]
        buffer2.append(salida)
        
    else: #toma la menor de las salidas para poder asignar al siguiente cliente 
          # a alguno de los dos servidores 
       if (servidor1 < servidor2): 
           servidor1.append(previo)
           b.insert(indice, max(salida,a[indice]))
           serv = -1*mu1*log(random.random())
           c.insert(indice, b[indice]+serv)
           salida = c[indice]
           buffer2.append(salida) 
           cont += 1 
           
       elif (servidor2 < servidor3):
           servidor2.append(previo)
           b.insert(indice, max(salida,a[indice]))
           serv = -1*mu2*log(random.random())
           c.insert(indice, b[indice]+serv)
           salida = c[indice]
           buffer2.append(salida)
           cont += 1 

       else:
           servidor3.append(previo) 
           b.insert(indice, max(salida,a[indice]))
           serv = -1*mu3*log(random.random())
           c.insert(indice, b[indice]+serv)
           salida = c[indice]
           buffer2.append(salida)
           cont += 1 
          
        
    if(cont <= cont_buffer1):        
       if previo in servidor1: 
          print("llego el client %2d" %(i)),
          print("llegada %6.3f" %(a[indice])),
          print("lo tendio el servidor 1" ),
          print("salida del primer servicio %6.3f" %(c[indice])),
          print("el cliente %2d esta entrando al segundo buffer" %(i)),
          print("----------------------------------")
        
       elif previo in servidor2:
          print("llego el client %2d" %(i)),
          print("llegada %6.3f" %(a[indice])),
          print("lo tendio el servidor 2" ),
          print("salida del primer servicio %6.3f" %(c[indice])),
          print("el cliente %2d esta entrando al segundo buffer" %(i)),
          print("----------------------------------")
        
       elif previo in servidor3:
          print("llego el cliente %2d" %(i)),
          print("llegada %6.3f" %(a[indice])),
          print("lo tendio el servidor 3" ),
          print("salida del primer servicio %6.3f" %(c[indice]))
          print("el cliente %2d esta entrando al segundo buffer" %(i)),
          print("----------------------------------")  
          
    else:
        print("soy el cliente %2d y fui rechazado por el primer buffer" %(i))
        rechazadosb1 += 1

print(" \n------ INICIA EL SEGUNDO BUFFER ----------\n")        

for j in range (len(buffer2)):
    indice = j%2
    if(j==0):
       entradas4.insert(indice,buffer2[indice]) 
       b2.insert(indice, max(salida2,buffer2[indice]))
       serv = -1*mu4*log(random.random())
       c2.insert(indice, b2[indice]+serv)
       salida = c2[indice]
       servidor4.append(salida2)
       d.insert(indice, c2[indice]-a2[indice])
       suma += d[indice]
       
    elif(j==1):
        entradas5.insert(indice,buffer2[indice])
        b2.insert(indice, max(salida2,buffer2[indice]))
        serv = -1*mu5*log(random.random())
        c2.insert(indice, b2[indice]+serv)
        salida = c2[indice]
        servidor5.append(salida2)
        d.insert(indice, c2[indice]-a2[indice])
        suma += d[indice]
        
    else:
        if (servidor4 < servidor5): 
           entradas4.insert(indice,buffer2[indice]) 
           b2.insert(indice, max(salida2,buffer2[indice]))
           serv = -1*mu4*log(random.random())
           c2.insert(indice, b2[indice]+serv)
           salida = c2[indice]
           servidor4.append(salida2) 
           d.insert(indice, c2[indice]-a2[indice])
           suma += d[indice]
           cont2 += 1 
           
        else:
            entradas5.insert(indice,buffer2[indice])
            b2.insert(indice, max(salida2,buffer2[indice]))
            serv = -1*mu5*log(random.random())
            c2.insert(indice, b2[indice]+serv)
            salida = c2[indice]
            servidor5.append(salida2)
            d.insert(indice, c2[indice]-a2[indice])
            suma += d[indice]
            cont2 += 1 
            
    if(cont2 <= cont_buffer2):         
       if salida2 in servidor4:
          print("se esta atendiendo el cliente %2d" %(j)),
          print("llegada del segundo buffer %6.3f" %(buffer2[indice])),
          print("inicio de servicio al pasar el segundo buffer %6.3f" %(b2[indice])),
          print("lo tendio el servidor 4" )
          print("termina %6.3f" %(c2[indice])),
          print("permanencia total %6.3f" %(d[indice])),
          print("salio cliente %2d" %(j)),
          print("----------------------------------")
        
       if salida2 in servidor5:
          print("se esta atendiendo el cliente %2d" %(j)),
          print("llegada del segundo buffer %6.3f" %(buffer2[indice])),
          print("inicio de servicio al pasar el segundo buffer %6.3f" %(b2[indice])),
          print("lo tendio el servidor 5" )
          print("termina %6.3f" %(c2[indice])),
          print("permanencia total %6.3f" %(d[indice])),
          print("salio cliente %2d" %(j)),
          print("----------------------------------")  
        
    else:
        print("soy el cliente %2d y fui rechazado por el segundo buffer" %(j))
        rechazadosb2 += 1
        
     
rechazados = rechazadosb1 + rechazadosb2 #total de clientes rechazados        
print("\ntotal de clientes rechazados", rechazados)
     
tiempo = suma / total_clientes    
print("\nEl tiempo promedio en el sistema es ", tiempo)






