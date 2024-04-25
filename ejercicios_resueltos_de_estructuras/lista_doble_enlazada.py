
class Nodo:
    def __init__(self,dato,siguiente=None,anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
        
class lista_doblemente_enlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def vacia(self):
        return self.primero == None
    
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            nuevo = Nodo(dato)
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1
        
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            nuevo = Nodo(dato)
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        self.size += 1
                
    def recorrer_inicio(self):
        if self.vacia():
            return False
        else:
            aux = self.primero
            while aux != None:
                print(aux.dato)
                aux = aux.siguiente
    
    def recorrer_final(self):
        if self.vacia():
            return False
        else:
            aux = self.ultimo
            while aux != None:
                print(aux.dato)
                aux = aux.anterior
    
    def eliminar_inicio(self):
        if self.vacia():
            return False
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None #Se produjo una excepción: AttributeError
                                        #'NoneType' object has no attribute 'anterior'
            self.size -= 1

    def eliminar_final(self):
        if self.vacia():
            return False
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1
        
    def Size(self):
        return self.size
        
        
