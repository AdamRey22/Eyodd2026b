from array import array as arr
#Importanto un archivo de otro archivo
from s02t0102_1d import print_array 

my_array = arr('i', [8, 11, 22, 27, 17, 22])

print("Antes de la eliminacion")
print_array(my_array)

# Eliminacion
my_array.remove(22)
print("Después de la eliminacion")
print_array(my_array)

valor_a_eliminar = 100

try:
    my_array.remove(valor_a_eliminar)
    print(f"El numero {valor_a_eliminar} fue eliminado.")
except:
    print(f"El número {valor_a_eliminar} no se encuentra en este arreglo.")

"""
print("Después de la inserción")
my_array.append(100)
print_array(my_array)

print("simular un appedn con insert")
my_array.insert(len(my_array), 90000)
print_array(my_array)
"""