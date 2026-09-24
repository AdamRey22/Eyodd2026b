"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100 
"""

#Importarmos biblioteca time
import time

 #Funcion que suma los 
 #primeros "n" numeros naturales 
 #en el def no se puede inicar con numeros, ni con gato
 #la funcion de _ se llama snake case
def sum_of_n( n):
    #: los dos puntos significa acontinuacion de la funcion
    total_sum = 0
        #Sumando los "n" numeros naturales con un ciclo for
        #ciclo for
    for number in range(1, n+1):
        total_sum = total_sum + number
    #Retornando el total de suma de los "n" numeros naturales        
    return total_sum    
#variable para guardar
#el data set

dataset = [] #[(n, time,sum), (n,time,sum)]
#Generando el contenido de dataset
for repetition in range(1,11):
    #Tomando el tiempo inical 
    timestamp_01 = time.time ()
    #Tomando tiempo 1 (INICIAl)
    n = repetition*500
    #guardo el tiempo final 
    result = sum_of_n(n)

    #⏱️Tomando el tiempo final 
    timestamp_02 = time.time ()

    elapsed_time = round ((timestamp_02-timestamp_01) * 1e6, 2)

    #Agregar la tripleta de los 
    #datos al dataset
    dataset.append( (n, elapsed_time, result) )
    # (n, elapsed_time, result) esto representa una tupla, que es un conjunto
    # de datos que no se puede modificar

for tup in dataset:
    print(tup)


#Programa que calcula las sumas
# de los "n" numeros naturales
#Se encapsula con For
#n = 500
#total_sum = 0
#Ciclo for, por cada de numero que hay de n+1 es imprimir
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
#print(f"La suma de los números del 1 al {n} es : {total_sum}")
#formato f, string con F, combinar los valores con f
#Impresion del tiempo de ejecucion en microsegundos
#print(f"Tiempo de ejecucion: {(timestamp_02-timestamp_01) * 1e6:.2f} μsegundos")