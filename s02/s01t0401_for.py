"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100 
"""

#Importarmos biblioteca time
import time

#Tomando el tiempo inical 
timestamp_01 = time.time ()

#Programa que calcula las sumas
# de los "n" numeros naturales

n = 100
total_sum = 0

# Ciclo for, por cada de numero que hay de n+1 es imprimir
for number in range(1, n+1):
    total_sum = total_sum + number
    #la primera vez que se ejecuta el ciclo
    #1: sum < - 0 + 1
    # sum = 1
    # 2: sum <- 1 + 2 
    # sum = 3
    # 3: sum <- 3 + 3
    #...
    #100: sum <- antSum_(-1) + 100
    #Asi tenemos los numeros sumados hasta 100
    #string permite combinar una salida con las variables 
print(f"La suma de los números del 1 al {n} es : {total_sum}")
#formato f, string con F, combinar los valores con f
#Tomando el tiempo final 
timestamp_02 = time.time ()

elapsed_time = (timestamp_02-timestamp_01) * 1e6

#Impresion del tiempo de ejecusion
print(f"Tiempo de ejecucion: {(timestamp_02-timestamp_01) * 1e6:.2f} μsegundos")
