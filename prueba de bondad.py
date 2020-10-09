# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:48:57 2020

@author: Adriana
"""
import numpy as np
import math

def fact(x=None):
    if(x == 0):
        return 1
    else:
        return (x*fact(x-1))

def probPoisson(lambd,evento):
    valor = 0
    contador = 0
    for i in range (evento + 1):
        valor = (((math.e)**(-lambd))*lambd**(i))/fact(i)
        contador = contador + valor
    probatxt.append(contador)  
    
     
alpha = 0.05

lambd = 0.0

Ti = 0
ti = []
t=0
Qt=0  #valores que van a ser menor o igual a t
Ro = 0 #valor que definira si se acepta Ho
muestra = [] #guarda los valores del txt 
probatxt = [] #guarda las probabilidades de los valores del txt
probatxt2 = [] #guarda las probabilidades repetidas para obtener las frecuencias esperadas 
frec_esperadas = [] #aqui se guardan las frecuencias esperadas totales
datos = [] #datos que se van a comparar 

frec = 0.0
frecuencias = {}

prob = 0.0

archivo = open("muestras.txt","r")

for i in archivo:
    muestra.append(int(i))
maximo = max(muestra)

for j in range(maximo+1):
    frecuencias[j] = muestra.count(j)

for j in range(len(frecuencias)):
    lambd = lambd + (j*(frecuencias[j]))

lambd = (lambd)/len(muestra)

print("lamda =",lambd)
print("alpha =",alpha)


j=0
for j in range(len(muestra)):
    prob = probPoisson(lambd,muestra[j])

probatxt2 = list(set(probatxt)) #obtiene las probabilidades de cada frecuencia 

k=0
for i in range (len(probatxt2)): #se multiplican las probabilidades por el numero de muestras
    frec = len(muestra)*probatxt2[i]
    frec_esperadas.append(frec)

#(frecuencia observada - frecuencia esperada)^2 entre frecuencia esperada ---- ontener el valor de t

for i in range(len(frecuencias)): #las frecuencias observadas
   for j in range(len(frec_esperadas)):
       Ti = ((frecuencias[i]-frec_esperadas[j])**2)/frec_esperadas[j]
       ti.append(Ti)
t += ti[i] #valor de t obtenido 

#print(len(ti))

datos = np.random.poisson(lambd,5000)

#uso del metodo del poisson para los datos obtenidos en el random 
j=0
for j in range(len(datos)):
    prob = probPoisson(lambd,datos[j]) 

j=0
for j in range(len(datos)):
    if(datos[i]<t):  #se comparan los datos obtenidos aleatoriamente con el valor de t
        Qt +=1   #si es menor o igual, se aumenta Qt
             
Ro = Qt/len(datos)  #se divide Qt entre los 5000 datos obtenidos 

#print("datos aleatorios",datos)
#print("Qt",Qt) 
#print("valor de t=",t)
print("Ro = ",Ro)
if (Ro<alpha): #si el dato obtenido es menor o igual al valor de alpha, entonces se acepta la hipotesis
   print("Se acepta Ho")        
else:
    print("Se rechaza Ho")  #si no, rechaza       
    
   