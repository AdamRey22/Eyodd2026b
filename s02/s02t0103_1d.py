from array import array as arr
#Importanto un archivo de otro archivo
from s02t0102_1d import print_array 

my_array = arr('i', [8, 11, 27, 17, 22])
print("Antes de la insercion")
print_array(my_array)

# Inserción
print("Después de la inserción")
my_array.insert(1,90)
print_array(my_array)

print("Después de la inserción")
my_array.append(100)
print_array(my_array)

print("simular un appedn con insert")
my_array.insert(len(my_array), 90000)
print_array(my_array)