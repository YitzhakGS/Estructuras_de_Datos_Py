#FIFO(Los primeros en entrar tambien son los primeros en salir)

class Cola:
    def __init__(self, size = 5):
        self.lista = []
        self.size = size
        self.tope = 0
        
    def empty(self):
        if self.lista == []:
            return True
        else:
            return False
    
    def push(self, dato):
        if self.tope < self.size:
            self.lista.append(dato)
            self.tope += 1
        elif self.tope == self.size:
            self.size += 5
            self.lista.append(dato)
            self.tope += 1
    
    def pop(self):
        if not self.empty():
            self.lista = self.lista[1:]
            self.tope -= 1
    
    def show(self):
        for i in range(self.tope-1,-1,-1):
            print(f"[{i}] -> {self.lista[i]}")
    
    def peek(self):
        if not self.empty():
            return self.lista[0]
    
    def peek_pop(self):
        elemento = self.peek()
        self.pop()
        return elemento
        



