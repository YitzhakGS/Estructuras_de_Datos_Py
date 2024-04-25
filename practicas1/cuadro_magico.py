matriz = [[0,0,0],[0,0,0],[0,0,0]]

print('introduce tres numeros enteros:  ')
a = int (input())
b = int (input())
c = int (input())
op = 0


bandera = True

for fila in range(len(matriz)):
    print('[', end=' ')
    
    for columna in range(len(matriz[fila])):
        
        if (fila == columna and (fila and columna) != 1):
            matriz[fila][columna] = a + b
            
            
        
    print(']')