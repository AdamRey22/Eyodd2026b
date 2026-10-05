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
n = 500
the_sum = 0 
#tomando el tiempo 
timestamp_01 = time.time()

#iniando la suma
# = es igual a que se le asigna un valor a una variable
while(n > 0):
    the_sum = the_sum + n # 100 + 99 + 98
    n = n - 1

#tomando el tiempo 2

timestamp_02 = time.time()

#imprimimos la solucion
print(f"La suma es: {the_sum}")

#CalculNDO EL TIEMPO DE EJECUCION

elapsed_time = round ((timestamp_02-timestamp_01) * 1e6, 2)
print(f"Tiempo de ejecución: {elapsed_time} μs")
