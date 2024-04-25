#algoritmo de ordenamiento por seleccion 
def seleccion(S):
    i = 0
    k = 0
    minimo = 0
    
    for i in range(len(S)-1):
        minimo = i 
        for k in range(i + 1, len(S)):
            if (S[k] < S[minimo]):
                minimo = k
        #cambio de variable 
        aux = S[i]
        S[i] = S[minimo]
        S[minimo] = aux
        print(S)
        
vector = [7, 19, 3, 20, 5]
print(vector)
seleccion(vector)


print('\0')

#algoritmo de insercion
def insercion(A):
    
    for i in range(len(A)):
        for j in range(i, 0, -1):
            print(A)
            if(A[j-1] > A[j]):
                aux = A[j]
                A[j] = A[j-1]
                A[j-1] = aux
                
    print(A)

A = [7, 19, 3, 20, 5]
#print(A)
#insercion(A)
