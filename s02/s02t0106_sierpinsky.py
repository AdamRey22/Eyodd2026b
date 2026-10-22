from array import array as arr

#Parametros de mi cuadricula 
rosw = 8
columns = 2 * rosw - 1 

# Creando la reticula 
matrix = []
#Construyendo el grid 
for row in range(rosw):
    new_row = arr("i", [0] * columns)
    matrix.append(new_row)

#Validando la construccion del Grid
print("Cantidad de filas:, {len(matrix)}")
print("Cantidad de columnas:, {len(matrix[0])}")

for row in matrix:
    print(list(row))