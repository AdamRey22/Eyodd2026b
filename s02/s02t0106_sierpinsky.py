from array import array as arr

# Parametros de mi cuadricula 
rows = 8
columns = 2 * rows - 1

#Funcion para imprimi rmatrix
def print_matrix(input_matrix):
    for row in matrix:
        print (list (row))

# Creando la reticula 
matrix = []

# Construyendo fel grid
for _ in  range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validadando la construccion del Grind
print (f"Cantidad de filas: {len(matrix)}")
print (f"Canitdad de columnas {len(matrix[0])}")



# Calculando el centro de la primera fila
center = columns // 2 #se hace divicion entera

#Estebleciendo el centro en 1
matrix [0][center] = 1

print_matrix (matrix)

#Se calcula el resto de la matrix 
#Siguiendo la logica del siperpinsky Gasket
for row in range (1, rows):
    for col in range(0, columns):
        left_upper_cell = 0
        right_upper_cell = 0

#si la columna es mayopr a cero
if col > 0:
    left_upper_cell = matrix[row - 1][col - 1]

#si la columna esta en el elemento antes del borde dercho
if col < columns - 1:
    right_upper_cell = matrix[row-1][col+1]

if left_upper_cell != right_upper_cell:
    matrix[row][col] = 1
else:
    matrix[row][col] = 0
print()
print_matrix(matrix)
#modificacion de = 
