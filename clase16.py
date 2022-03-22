#from collection import *

#from collections import namedtuple, Counter


#Fish = namedtuple( "Fish", ["name", "species", "tank"])

#Esto crea una clase pez con los atributos nombre, especie y tanque.

#miPrimerPez = Fish ("Sammy", "Tiburon", "tanque grande")

#print (miPrimerPez)

#print (miPrimerPez._asdict())

#lista = [1,2,3,4,4,3,7,6,3,7]

#print (Counter(lista))

#chain = "Hola esta es una prueba de Python, Hola Mundo"

#print (Counter(chain))

#print (Counter (chain.split()))

from datetime import datetime, timedelta, timezone


#dt = datetime.now()

#print (dt)

#print (dt.year)
#print (dt. month)
#print (dt.day)
#print (dt.hour)
#print (dt.minute)
#print (dt.second)
#print (dt.microsecond)

#dt = datetime (2000,1,1)

#print (dt)

#print (dt.replace (year = 3000))
#print (dt.strftime ("%A %d %B %Y %I:%M"))

#t= timedelta (days = 14, hours = 4, seconds = 1000)
#dentro_de_dos_semanas = dt + t

#print (dentro_de_dos_semanas)


from mi_primer_repositorio.fechas import calculo_fecha_cumple


#calculo_fecha_cumple ("2021/10/6")

import math

#value = math.sqrt(9)

#print ("La raiz cuadrada es:" , value)

#value = math.ceil (1.4)
#value_two = math.floor(1.4)

#print (f"Primer redondeo:{value}")

#print (f"Segundo redondeo:{value_two}")

import random

#print (random.randrange(20,50))
#print (random.randrange(20, 50, 7))


#lista = [1,2,"Juan",4,"Pepe",6]

#print (random.choice(lista))
