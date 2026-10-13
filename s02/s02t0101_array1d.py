import array as arr
my_array = arr.array ('i',[10, 300, 3, 7, 40, 55, 654, 22, 17])

print(f"localizando 22: {my_array.index(22)}")

num_to_search = 200

try:
  print(f"Localizado {num_to_search}: {my_array.index(num_to_search)}")
except:
  print("⚠️ Numero no encontrado!!!")