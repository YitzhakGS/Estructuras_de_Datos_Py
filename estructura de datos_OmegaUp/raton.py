
from collections import deque

def encontrar_camino(matriz):
    if not matriz or not matriz[0]:
        return None
    
    N = len(matriz)
    
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    letras_movimiento = ['D', 'U', 'R', 'L'] 
    cola = deque([(0, 0, [(0, 0), ''])]) 
    visitados = set() 
    caminos = []  
    
    while cola:
        fila, columna, camino_actual = cola.popleft()

        visitados.add((fila, columna))

        if fila == N - 1 and columna == N - 1:
            caminos.append(camino_actual)
        
        for i, (dr, dc) in enumerate(direcciones):
            nueva_fila, nueva_columna = fila + dr, columna + dc
            
            if (0 <= nueva_fila < N and 0 <= nueva_columna < N and
                    matriz[nueva_fila][nueva_columna] == 1 and
                    (nueva_fila, nueva_columna) not in visitados):
                nuevo_camino = list(camino_actual[0])
                nuevo_camino.append((nueva_fila, nueva_columna))
                nuevo_camino_letras = camino_actual[1] + letras_movimiento[i]
                cola.append((nueva_fila, nueva_columna, (nuevo_camino, nuevo_camino_letras)))

    return caminos

matriz = []

n = int(input(''))

for i in range(n):
    fila = [int(item) for item in input("").split()]
    matriz.append(fila)

caminos = encontrar_camino(matriz)
if caminos:
    print(f"{len(caminos)}")
    for i, (camino_coords, camino_letras) in enumerate(caminos):
        print(f"{camino_letras}")
else:
    print("-1")
