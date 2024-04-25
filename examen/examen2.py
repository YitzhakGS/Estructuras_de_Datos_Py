from pila import Pila
print("defina un limite: ")
max = int(input())
origen = Pila(max)
copia = Pila(max)
destino = Pila(max)
registro = input()
for i in range(len(registro)):
    origen.push(registro[i])

copia = origen

while not origen.empty():
    elemento = origen.peek()
    destino.push(elemento)
    origen.pop()
    
print("pila 1:")
origen.show()
print("\n")
print("pila 2:")
destino.show()
print("\n")
print("elementos que tenia la pila origen:")
copia.show()