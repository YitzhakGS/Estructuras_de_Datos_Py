
n = [int(item) for item in input("").split()]
F,C = n
tablero_enteros = []
tablero_final = []
for i in range(F):
    fila = input()
    fila_enteros = [0 if item == "." else item for item in fila]
    tablero_enteros.append(fila_enteros)

for fila in range(F):
    for celda in range(C):
        if tablero_enteros[fila][celda] == "*":
            x = fila
            y = celda
            if x + 1 < F:
                tablero_enteros[x + 1][y] += 1
            if x - 1 >= 0:
                tablero_enteros[x - 1][y] += 1
            if y + 1 < C:
                tablero_enteros[x][y + 1] += 1
            if y - 1 >= 0:
                tablero_enteros[x][y - 1] += 1
            if x + 1 < F and y + 1 < C:
                tablero_enteros[x + 1][y + 1] += 1
            if x - 1 >= 0 and y - 1 >= 0:
                tablero_enteros[x - 1][y - 1] += 1
            if x - 1 >= 0 and y + 1 < C:
                tablero_enteros[x - 1][y + 1] += 1
            if x + 1 < F and y - 1 >= 0:
                tablero_enteros[x + 1][y - 1] += 1

for i in range(F):
    fila_string = ''.join(map(str, tablero_enteros[i]))
    tablero_final.append(fila_string)

for fila in tablero_final:
    print(fila)


