
numeros = [12, 36, 72, 81]
numeros.sort()

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"la posicion {indice} con el valor: {valor}")
#el valor que retorna el for es una tupla

lista = []
indice = 0

Total_num = input("de cuantos nuemros quieres la lista: ")

while indice < int(Total_num):
    lista.append(valor)
    indice+=1

for num in lista:
    resultado = int(num) * 2
    print(resultado)
    
print(lista)