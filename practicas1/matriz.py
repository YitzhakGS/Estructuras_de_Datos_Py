matriz=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

for fila in matriz:
    print('[', end=' ')
    for celda in fila:
        print(celda, end=' ')
    print(']')
    
print('\0')
#multiplicacion de la matriz original
for fila in range(len(matriz)):
    print('[', end=' ')
    
    for celda in range(len(matriz[fila])):
        multiplicacion = matriz[fila][celda]*5
        print(multiplicacion, end=' ')
        
    print(']')

#matrizR vacia 
matrizR = [ [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
#matrizA 
matriz=[[5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]]


print('\0')
#trabajo con las filas 
for fila in range(len(matriz)):
    suma = 0
    for celda in range(len(matriz[fila])):
        suma += matriz[fila][celda] 
        matrizR[fila][celda] = matriz[fila][celda]
        matrizR[fila][celda + 1] = suma
#trabajo con las columnas
for columna in range(len(matriz)):
    suma = 0
    for fila in range(len(matriz[columna])):
        suma += matriz[fila][columna] 
        matrizR[fila][columna] = matriz[fila][columna]
        matrizR[fila + 1][columna] = suma
        
#hat un error a la hora de poner el valor en la posicion [3][3] 
#for fila in range(len(matrizR)):
#    suma = 0
#    for celda in range(len(matrizR[fila])):
#       if fila == celda:
#            suma += matrizR[fila][celda]
#            matrizR[3][3] = suma


#imprimo la matrizR
for fila in matrizR:
    print('[', end=' ')
    
    for celda in fila:
        print(celda, end=' ')
        
    print(']')






