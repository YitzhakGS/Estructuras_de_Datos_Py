class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = Nodo

class Lista_circular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacio(self):
        return self.primero == None
    
    def agregar_inicio(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.next = self.primero
        else:
            nuevo = Nodo(dato)
            nuevo.next = self.primero
            self.primero = nuevo
            self.ultimo.next = self.primero
    
    def agregar_final(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.next = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.next = Nodo(dato)
            self.ultimo.next = self.primero
    
    def recorrer_cantidad(self, elementos):
        if self.vacio():
            return False
        else:
            aux = self.primero
            contador = 0
            while contador < elementos:
                print(aux.dato)
                aux = aux.next
                contador += 1
                
    def recorrer_ciclo(self):
        if self.vacio():
            return False
        else:
            aux = self.primero
            while aux.next != self.primero:
                print(aux.dato)
                aux = aux.next
            print(aux.dato)
            
    def eliminal_inicio(self):
        if self.vacio():
            return False
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.next
            self.ultimo.next = self.primero
        
    def eliminar_final(self):
        if self.vacio():
            return False
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.next != self.ultimo:
                aux = aux.next
            aux.next = self.primero
            self.ultimo = aux



