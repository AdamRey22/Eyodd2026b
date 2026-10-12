import array as arr
#creacion de un arreglo
#i = Entero con signo
#Numero Decimal 
#Numero decimal doble
#Caracteres unicode
my_array = arr.array ('i',[10, 22, 300, 3, 7, 40, 55, 654, 22])

#iteraccion automatica
for num in my_array:
#   print(num)

#Acceso individual a los elementos
#print(my_array[0]) #Primer elemento
#print(my_array[1]) #Segundo elemento
#print(my_array[2]) #Tercer elemento

#Tamaño de un arreglo
#Lenght
#print(len(my_array))

#Iteraccion de indices
 for i in range(len(my_array)):
    if my_array[i] % 2 == 0:
        print(f"Elemento num {i+1}: {my_array[i]}")
#sesion lunes