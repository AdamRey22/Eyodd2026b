# Array
# from array import 
import array as arr

# Creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble
# u: Caracteres unicode
my_array = arr.array('i', [10, 300, 3, 7, 40, 55, 654, 22, 17])

# Interaccion automatica
"""
for num in my_array:
    print(num)
"""

# Accerso indivial a los elementos
"""
print(my_array[0]) # primer elemento 
print(my_array[1]) # segundo elemento 
print(my_array[2]) # tercer elemento 
"""

# Tamano de un arreglo
# length
"""
print (len(my_array))
"""

# Interaccion por indices 
"""
for i in range (len(my_array)):
    print(f"Elemento {i+1}: {my_array[i]}")
"""

"""
for i in range (len(my_array)):
    if my_array[i] % 2 == 0:    
        print(f"Elemento Num {i+1}: {my_array[i]}")
"""

# Busqueda de un elemento 
print(f"Localizando 22: {my_array.index(22)}")

num_to_search = 22

try:
    print(f"Localizado {num_to_search}: {my_array.index(num_to_search)}")
except:
    print("⚠️ Numero no encontrado!!!")

# Modificando un valor usando
# bracket notation (cambiando el último elemento, índice 8, a 22)
my_array[8] = 22

try:
    print(f"Localizando 200: {my_array.index(200)}")
except:
    print("⚠️ Numero no encontrado!!!!")

# Asignado valor en un indice que no existe
try:
    my_array[100] = 3 
except:
    print("⚠️ Inidice no existe!!!")
#sesion martes 13/10/2026