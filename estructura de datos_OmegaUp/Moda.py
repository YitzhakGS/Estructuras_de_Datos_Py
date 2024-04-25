n = int(input())
lista = [int(item) for item in input("").split()]
contador_Mayor = 0
for i in range(len(lista)):
    llave = lista[i]
    contador = 1
    for j in range(i + 1, len(lista)):
        if llave == lista[j]:
            contador += 1
            num_Mayor = lista[j]
    if contador > contador_Mayor:
        contador_Mayor = contador
        
print(num_Mayor)
    