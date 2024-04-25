import random as rand

arreglo=[]
suma = 0.0

for indice in range(100):
    arreglo.append(rand.randrange(0,100))

print(arreglo)

for indice in range(len(arreglo)):
    suma = suma + arreglo[indice]

promedio = suma/len(arreglo)

print(f"el promedio es: {promedio}")