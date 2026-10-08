#Importando el modulo arrays:
from array import array as arr

#Creando un arregloo:
array_01 = arr('i', [3, 8, 5, 1 , 6])

#iterando automáticamente sobre el arreglo...
for data in array_01:
    print(data, end = ",")
print()