
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        
class lista_circular_doble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar_primero(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            nuevo = Nodo(dato)
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        self.unir_nodos()
            
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            nuevo = Nodo(dato)
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.unir_nodos()
    
    def unir_nodos(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
        
    def recorrer_inicio_a_fin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
    
    def recorrer_fin_a_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break
            
    def eliminar_primero(self):
        if self.vacia():
            return False
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.unir_nodos()
            
    def eliminar_ultimo(self):
        if self.vacia():
            return False
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.unir_nodos()
            
    
    def buscar(self, valor):
        if self.vacia():
            return False
        else:
            aux = self.primero
            while aux:
                if aux.dato == valor:
                    return aux
                    break
                else:
                    aux = aux.siguiente
                    if aux == self.primero:
                        return False
            



