filas_matriz_principal, columnas_matriz_principal = map(int, input().split())
matriz_principal = []
for _ in range(filas_matriz_principal):
    fila = list(map(int, input().split()))
    matriz_principal.append(fila)

filas_matriz_buscar, columnas_matriz_buscar = map(int, input().split())
matriz_buscar = []
for _ in range(filas_matriz_buscar):
    fila = list(map(int, input().split()))
    matriz_buscar.append(fila)
    
def encontrar_coincidencias(matriz_principal, matriz_buscar):
    n, m = len(matriz_principal), len(matriz_principal[0])
    p, q = len(matriz_buscar), len(matriz_buscar[0])
    coincidencias = []

    for i in range(n - p + 1):
        for j in range(m - q + 1):
            es_coincidencia = True
            for x in range(p):
                for y in range(q):
                    if matriz_principal[i + x][j + y] != matriz_buscar[x][y]:
                        es_coincidencia = False
                        break
                if not es_coincidencia:
                    break
            if es_coincidencia:
                coincidencias.append((i, j))
    return coincidencias

resultados = encontrar_coincidencias(matriz_principal, matriz_buscar)

for resultado in resultados:
    print(resultado)
