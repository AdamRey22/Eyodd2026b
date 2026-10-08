# Creamos una lista de estudiantes

student_list_01 = ['Jordan','Pipen','Curry','Shack']

def random_function(students):
    first = students[0] #O(1).
    total = 0 #O(1)
    new_list = [] #O(1)

    for student in students:
        total += 1 #O(n)
        new_list.append(student) #O(n)

    print(new_list) #O(1)
    return total #O(1)

print (f"Tamaño de lista: {len(student_list_01)}")
print(random_function(student_list_01))
print("")

# Calcular O(2n)+O(5) = 0(2n+5)= O(n)
