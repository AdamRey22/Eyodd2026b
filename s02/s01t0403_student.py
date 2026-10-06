"""
NOTAS:
1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes
2. Es ver cuanto crece el numero de 
operaciones en mi algoritmo conforme
creece el tamaño de la entrada 
Agrego las bigO identificadas
Teniendo en cuenta la cOta superior asintotica
O(n) + 4*O(1) = O(n+4) = O(n)
"""
#creando una lista de estudiantes
student_list_01 = ['Val', 'Omar', 'Liz', 'Raziel']
student_list_02 = ['Luis', 'Mauricio', 'Santiago', 'Donovan']

#Verificando presencia de los estudiantes
def check_student(input_student, student_list):
    #un for va casilla por casilla
    for student in student_list:
        if input_student == student: #O(n) 
            print("🟢 Estudiante encontrado") #O(1) 
            return student #O(1)
    #pero si no se encuentra el estudiante
    print("🔴 Estudiante no encontrado") #tiene complejidad constante O(1)
    return None
#probando algoritmo
check_student('Omar', student_list_02)

