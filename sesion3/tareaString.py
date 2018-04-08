entrada = raw_input("Introduce texto: ")
diccionario = {}
contador = 0
for letra in entrada:
	if "a" in letra:
		contador = contador + 1
print("La cantidad de caracteres 'A' son: ")
print(contador)