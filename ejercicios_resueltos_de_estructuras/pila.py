#es una pila estatica con una lista
#a la cual se le pasa el valor de la longitud de la lista

class Pila:
    
    def __init__(self, size):
        self.lista = []
        self.size = size
        self.tope = 0
    
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False

    def push(self, dato):
        if self.size > self.tope:
            self.lista.append(dato)
            self.tope+=1
        else:
            print("se llego al tope de la pila")
            #para hacer la pila dinamica se puede incrementar el valor de size
    
    def pop(self):
        if self.empty():
            print("la pila esta vacia")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]
    
    def show(self):
        for i in range(self.tope-1,-1,-1):
            print(f"[{i}] -> {self.lista[i]}")
    
    def peek(self):
        if not self.empty():
            return self.lista[self.tope - 1]
        else:
            print("La pila está vacía")
