def encontrar_camino(matriz):
    if not matriz or not matriz[0]:
        return None
    
    N = len(matriz)

    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    letras_movimiento = ['D', 'U', 'R', 'L'] 
    
    def dfs(fila, columna, camino_actual):
        
        if fila == N - 1 and columna == N - 1:
            caminos.append(camino_actual)
            return
        
        for i, (dr, dc) in enumerate(direcciones):
            nueva_fila, nueva_columna = fila + dr, columna + dc

            if (0 <= nueva_fila < N and 0 <= nueva_columna < N and
                    matriz[nueva_fila][nueva_columna] == 1 and
                    (nueva_fila, nueva_columna) not in visitados):
                visitados.add((nueva_fila, nueva_columna))
                nuevo_camino = list(camino_actual)  
                nuevo_camino.append(letras_movimiento[i]) 
                dfs(nueva_fila, nueva_columna, nuevo_camino)
                visitados.remove((nueva_fila, nueva_columna))  
    
    caminos = [] 
    visitados = set() 
    
    visitados.add((0, 0))
    dfs(0, 0, [])
    
    return caminos

matriz = []

n = int(input(''))

for i in range(n):
    fila = [int(item) for item in input("").split()]
    matriz.append(fila)

caminos = encontrar_camino(matriz)
if caminos:
    print(f"{len(caminos)}")
    for i, camino_letras in enumerate(caminos):
        print(f"{''.join(camino_letras)}")
else:
    print(-1)
