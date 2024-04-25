
class Nodo:
    def __init__(self,dato,next=None):
        self.dato = dato
        self.next = next
        
#   cada que pongo un mensaje de que la lista esta vacia o estan mal los datos
#   puedo agregar excepciones 
#       raise ValueError("la lista esta vacia o estan mal los datos") 
        
class lista_simple:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def vacia(self):
        return self.head == None
    
    def es_primero(self, nodo):
        if self.vacia():
            return False
        else:
            if (nodo == self.head) and (nodo.dato == self.head.dato):
                return True
    
    def es_ultimo(self, nodo):
        if self.vacia():
            return False
        else:
            if (nodo == self.tail) and (nodo.dato == self.tail.dato):
                return True

    def agregar_ultimo(self,dato):
        if self.vacia() == True:
            self.head = self.tail = Nodo(dato)
        else:
            nuevo = self.tail
            self.tail = nuevo.next = Nodo(dato)

    def agregar_inicio(self,dato):
        if self.vacia() == True:
            self.head = self.tail = Nodo(dato)
        else:
            nuevo = Nodo(dato)
            nuevo.next = self.head
            self.head = nuevo
            
    def imprimir(self):
        if self.vacia():
            print("la lista esta vacia")
        else:
            aux = self.head
            while aux != None:
                print(f"{aux.dato} =>", end=" ")
                aux = aux.next
                
    def eliminar_ultimo(self):
        if self.vacia():
            print("la lista esta vacia")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:    
            aux = self.head
            while aux.next != self.tail:
                aux = aux.next
            aux.next = None
            aux = self.tail
                
    def eliminar_primero(self):
        if self.vacia():
            print("la lista esta vacia")
        else:
            aux = self.head
            self.head = aux.next
            del aux
        
    def encontrar_anterior(self, search):
        if self.vacia():
            print("la lista esta vacia")
        else:
            aux = self.head
            if aux.dato == search:
                return aux
            while aux.next is not None:
                siguiente_nodo = aux.next
                if siguiente_nodo.dato == search:
                    return aux
                aux = aux.next 
            return False
    
    def agregar_despues_de(self, dato, dato_nuevo):
        nodo_actual = self.head

        while nodo_actual is not None and nodo_actual.dato != dato:
            nodo_actual = nodo_actual.next
            
        if nodo_actual is None:
            print(f"No se encontró el nodo con el valor {dato} en la lista.")
        else:
            nuevo_nodo = Nodo(dato_nuevo)
            nodo_siguiente = nodo_actual.next

            if nodo_siguiente is None:
                self.agregar_ultimo(dato_nuevo)
            else:
                nodo_actual.next = nuevo_nodo
                nuevo_nodo.next = nodo_siguiente

    
    def eliminar_por_valor(self, dato):
        nodo_anterior = self.encontrar_anterior(dato)
        if self.vacia() or (nodo_anterior == (None or False)):
            print("la lista esta vacia o ingreso mal los datos")
        
        else:
            nodo = nodo_anterior.next
            
            if nodo is None:
                self.eliminar_ultimo()
            elif self.es_primero(dato):
                self.eliminar_primero()
            else:
                self.eliminar_nodo_intermedio(nodo_anterior, nodo)

    def eliminar_nodo_intermedio(self, nodo_anterior, nodo):
        nodo_siguiente = nodo.next
        nodo_anterior.next = nodo_siguiente
        del nodo

