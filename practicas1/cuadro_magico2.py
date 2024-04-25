matriz = [[0,0,0],[0,0,0],[0,0,0]]

print('introduce tres numeros enteros:  ')
#de esta manera puedo introducir numeros enteros por teclado 
a = int (input())
b = int (input())
c = int (input())


matriz[0][0] = int(a + b)
matriz[0][1] = int(a - (b + c))
matriz[0][2] = int(a + c)
matriz[1][0] = int(a - (b - c))
matriz[1][1] = int(a)
matriz[1][2] = int(a + (b - c))
matriz[2][0] = int(a - c)
matriz[2][1] = int(a + (b + c))
matriz[2][2] = int(a + b)

for fila in matriz:
    print('[', end=' ')
    for celda in fila:
        print(celda, end=' ')
    print(']')
