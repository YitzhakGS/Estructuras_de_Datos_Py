
from cola import Cola

class Nodo:
    def __init__(self, dato=None, parent=None, is_root=False, es_menor=False, es_mayor=False, nivel=None):
        self.dato = dato
        self.parent = parent
        self.is_root = is_root
        self.es_menor = es_menor
        self.es_mayor = es_mayor
        self.izquierda = None
        self.derecha = None
        self.nivel = nivel
        
class Arbol_Binario:
    def __init__(self):
        self.root = None
    
    def vacio(self):
        if self.root == None:
            return True
        else:
            return False

    def agregar_nodo(self, dato):
        if self.vacio():
            self.root = Nodo(dato = dato, is_root=True, nivel=0)
        else:
            nodo = self.posicion_nueva(dato)
            if dato <= nodo.dato:
                nodo.izquierda = Nodo(dato=dato, parent=nodo, es_menor=True, nivel = (nodo.nivel)+1 ) 
            else: 
                nodo.derecha = Nodo(dato=dato, parent=nodo, es_mayor=True, nivel = (nodo.nivel)+1 )
            
#   con esta fucion identifica el nodo padre del nuevo nodo 
#   dependiendo si es menor o mayor que la raiz 
    def posicion_nueva(self, dato):
        aux = self.root
        while aux is not None:
            padre = aux 
            if dato <= aux.dato:
                aux = aux.izquierda
            else:
                aux = aux.derecha
        return padre
    
    def buscar(self,nodo,valor):
        if not nodo:
            return False
        elif nodo.dato == valor:
            return nodo
        elif valor <= nodo.dato:
            return self.buscar(nodo.izquierda, valor)
        else:
            return self.buscar(nodo.derecha, valor)
        
    def recorrido_DFS(self, nodo):
        nodos_visitados = []
        if nodo:
            nodos_visitados.append(nodo.dato)
            nodos_visitados.extend(self.recorrido_DFS(nodo.izquierda))
            nodos_visitados.extend(self.recorrido_DFS(nodo.derecha))
        return nodos_visitados
    
    def recorrido_BFS(self, nodo):
        c = Cola()
        c.push(nodo)
        nodos_visitados = set() #conjunto desordenado de elementos unicos
        nodos = []
        while not c.empty():
            nodo_actual = c.peek_pop()
            if nodo_actual not in nodos_visitados:
                nodos.append(nodo_actual.dato)
                nodos_visitados.add(nodo_actual)
                if nodo_actual.izquierda:
                    c.push(nodo_actual.izquierda)
                if nodo_actual.derecha:
                    c.push(nodo_actual.derecha)
        return nodos
    
    def hermanos(self, nodo):
        niveles = {}
        lista = self.recorrido_BFS(nodo)
        for valor in lista:
            elemento = self.buscar(nodo, valor)
            nivel = elemento.nivel
            if nivel in niveles:
                niveles[nivel].append(elemento.dato)
            else:
                niveles[nivel] = [elemento.dato]
        return niveles
    
    def padres(self, root):
        padres = {"Raiz": []}
        lista = self.recorrido_BFS(root)
        for valor in lista:
            elemento = self.buscar(root, valor)
            nivel = elemento.nivel
            if nivel != 0:
                if elemento.parent.dato in padres:
                    padres[elemento.parent.dato].append(elemento.dato)
                else:
                    padres[elemento.parent.dato] = [elemento.dato]
            else:
                padres["Raiz"].append(elemento.dato)
        return padres
    
    def grado(self, root):
        lista = self.recorrido_BFS(root)
        for valor in lista:
            elemento = self.buscar(root, valor)
            grado = 0
            if elemento.izquierda:
                grado += 1
            if elemento.derecha:
                grado += 1
                
            if grado == 0:
                print(f"Nodo hoja: [{elemento.dato}]")
            else:
                print(f"Nodo: [{elemento.dato}] --> Grado: {grado}")
        
#   recorridos de el arbol
    def in_order(self,nodo):
        if nodo:
            self.in_order(nodo.izquierda)
            print(nodo.dato)
            self.in_order(nodo.derecha)
            
    def pre_order(self,nodo): #busqueda en profundidad
        if nodo:
            print(nodo.dato)
            self.pre_order(nodo.izquierda)
            self.pre_order(nodo.derecha)
    
    def pos_order(self,nodo):
        if nodo:
            self.pos_order(nodo.izquierda)
            self.pos_order(nodo.derecha)
            print(nodo.dato)

#pagina 295 ejer 5 y pag 248 ejer 1-2

#EL AMANECER DE LOS JEDI
#LA EDAD DORADA DE LOS SITH
#LA CAIDA DE LOS SITH
