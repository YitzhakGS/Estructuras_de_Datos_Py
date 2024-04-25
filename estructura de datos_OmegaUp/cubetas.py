nuemeros = [int(item) for item in input("").split()]
num_E, num_S = nuemeros
colores = [int(item) for item in input("").split()]
ordenados = []
for i in range(num_E):
    contador = 0
    llave = i + 1
    for j in range(num_E):
        if llave == colores[j]:
            contador += 1
    ordenados.append(contador)

for i in range(num_S):
    print(f"{i + 1}: {ordenados[i]}")