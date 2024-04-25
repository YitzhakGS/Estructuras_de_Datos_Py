def contar_minas_adyacentes(tablero, fila, columna):
    direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    minas = 0
    for d in direcciones:
        x, y = fila + d[0], columna + d[1]
        if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] == '*':
            minas += 1
    return minas

def buscaminas(M, N, tablero):
    resultado = []

    for fila in range(M):
        nueva_fila = ''
        for columna in range(N):
            if tablero[fila][columna] == '*':
                nueva_fila += '*'
            else:
                minas_adyacentes = contar_minas_adyacentes(tablero, fila, columna)
                nueva_fila += str(minas_adyacentes)
        resultado.append(nueva_fila)

    return resultado

try:
    M, N = map(int, input().split())
    tablero = []

    for _ in range(M):
        fila = input()
        tablero.append(fila)

    resultado = buscaminas(M, N, tablero)

    for fila in resultado:
        print(fila)

except Exception as e:
    print("Error:",e)