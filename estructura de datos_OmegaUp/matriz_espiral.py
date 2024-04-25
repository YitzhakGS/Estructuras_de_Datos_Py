
n = int(input())
m = int(input())
matriz = []
nueva_lista = []
fila_inicio = 0
fila_final = n - 1
columna_inicio = 0
columna_final = m - 1

for i in range(n):
    fila = [int(item) for item in input("").split()]
    matriz.append(fila)


while (fila_inicio <= fila_final) and (columna_inicio <= columna_final):
    
    for columna in range (columna_inicio, columna_final + 1):
        nueva_lista.append(matriz[fila_inicio][columna])
    fila_inicio += 1    
    
    for fila in range(fila_inicio, fila_final + 1):
        nueva_lista.append(matriz[fila][columna_final])
    columna_final -= 1
    
    if fila_inicio <= fila_final:
        for columna in range(columna_final, columna_inicio - 1, -1):
            nueva_lista.append(matriz[fila_final][columna])
        fila_final -= 1
    
    if columna_inicio <= columna_final:
        for fila in range(fila_final, fila_inicio-1, -1):
            nueva_lista.append(matriz[fila][columna_inicio])
        columna_inicio += 1
    
print(','.join(map(str, nueva_lista)))