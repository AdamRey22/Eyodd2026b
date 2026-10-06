"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100 
"""
#importar la biblioteca time
import time

#Crear las variables para
# el problema 
def sum_of_n( n):
 the_sum = 0 
 while n > 0:
    the_sum = the_sum + n
    n = n - 1
 return the_sum    

dataset = []

repetition = 1
while repetition <= 10:
    
    timestamp_01 = time.time ()

    n = repetition*500
    
    result = sum_of_n(n)

    #⏱️
    timestamp_02 = time.time ()

    elapsed_time = round ((timestamp_02-timestamp_01) * 1e6, 2)

    dataset.append( (n, elapsed_time, result) )
    # (n, elapsed_time, result) esto representa una tupla, que es un conjunto
    # de datos que no se puede modificar
    repetition = repetition + 1

#CalculNDO EL TIEMPO DE EJECUCION

elapsed_time = round ((timestamp_02-timestamp_01) * 1e6, 2)
print(f"Tiempo de ejecución: {elapsed_time} μs")

while dataset: 
   print (dataset.pop(0))