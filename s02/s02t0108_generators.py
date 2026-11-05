# Los generadores son funciones que pueden
# pausar su ejecución.

# Cuando se invoca una funcion generadora
# devuelve un objeto generador (aka Iterador)

# El codigo dentro de la funcion no se ejecuta
# de inmediato, solo se compila.

# La funcion se ejecuta unicamente cuando
# iteras sobre el generador.

def my_generator():
    yield 1 
    yield 2 
    yield 3
    yield 4
#se invoca funcion generadora 
my_iterator = my_generator()

#se itera manualmente sobre el generador 
#print(next(my_iterator))
#print(next(my_iterator))
#print(next(my_iterator))
#print(next(my_iterator))

#los iteratores se puede iterar con un for
for value in my_iterator:
    print(value)
