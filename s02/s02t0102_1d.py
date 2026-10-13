from array import array as arr
def print_array(input):
    print ("[", end="")
    for element in input:
        print(element, end=" ")
    print("\b]")    
my_array = arr('i', [8, 11, 27, 17, 22])
print_array(my_array)

#Buscar el, elemento 17 en el arreglo
number_to_search = 20
for integer in my_array:
    if integer == number_to_search:
        print("🙀 numero enconytrado")
        break #sirve para salirse de un ciclo
    counter+=1
    if counter == len(my_array):
        print("😿 numero no encontrado")
#sesion Martes jeje