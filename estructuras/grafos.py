#dijkstra
#BFS, DFS
from cola import Cola

class Graph:
    def __init__(self, Nodos, dirijido = False):
        self.Nodos = Nodos
        self.aristas = {}
        self.dirijido = dirijido

        for nodo in self.Nodos:
            self.aristas[nodo] = []
    
    def grado(self):
        grados = {}
        for nodo, aristas in self.aristas.items():
            grado = len(aristas)
            grados[nodo] = grado
        return grados

    def imprimir_aristas(self):
        for nodo in self.Nodos:
            print(f"[{nodo}] --->",self.aristas[nodo])

    def unir_nodos(self, nodoA, nodoB, peso = None):
        self.aristas[nodoA].append((nodoB, peso))
        if not self.dirijido:
            self.aristas[nodoB].append((nodoA, peso))

    def Dijktra(self,nodo_inicial, nodo_final):
        nodos_no_visitados = set(self.Nodos)
        distancias = {nodo: float('inf') for nodo in self.Nodos}
        distancias[nodo_inicial] = 0
        padres = {nodo: None for nodo in self.Nodos}

        while nodos_no_visitados:
            nodo_actual = min(
                nodos_no_visitados,
                key=lambda n: distancias[n]
            )

            adyacentes = self.nodos_adyacentes(nodo_actual)

            for nodo_a, peso in adyacentes:
                distancia_acumulada = distancias[nodo_actual] + peso

                if distancia_acumulada < distancias[nodo_a]:
                    distancias[nodo_a] = distancia_acumulada
                    padres[nodo_a] = nodo_actual

            nodos_no_visitados.remove(nodo_actual)

        # Imprimir el camino
        camino = self.construir_camino(nodo_inicial, nodo_final, padres)
        if camino is not None:
            print(f"Camino de {nodo_inicial} a {nodo_final}: {camino}")
    
    def construir_camino(self, nodo_inicial, nodo_final, padres):
        camino = [nodo_final]
        while camino[-1] != nodo_inicial:
            padre = padres.get(camino[-1])
            if padre is None:
                print(f"No hay camino de {nodo_inicial} a {nodo_final}")
                return None
            camino.append(padre)
        return ' -> '.join(reversed(camino))

    def calcular_peso(self, nodoA, nodoB):
        for nodo, peso in self.aristas[nodoA]:
            if nodo == nodoB:
                return peso
        return float('inf')            
    
    def salidas(self, nodo):
        return len(self.aristas[nodo])
    
    def nodos_adyacentes(self,nodo):
        adyacentes = []
        for vecino, peso in self.aristas[nodo]:
            adyacentes.append((vecino,peso))
        return adyacentes
    
    def recorrido_BFS(self, nodo_inicial):
        c = Cola()
        visitados =  set()
        nodos = []
        c.push(nodo_inicial)
        while not c.empty():
            nodo_actual = c.peek_pop()
            if nodo_actual not in visitados:
                nodos.append(nodo_actual)
                visitados.add(nodo_inicial)
                for vecinos,_ in self.nodos_adyacentes(nodo_actual):
                    if vecinos not in  visitados:
                        c.push(vecinos)
        return nodos
    
    def recorrido_DFS(self, nodo_inicial):
        visitados = set()

        def dfs_recursivo(nodo):
            print(nodo, end=' ')
            visitados.add(nodo)
        
            for vecino, _ in self.nodos_adyacentes(nodo):
                if vecino not in visitados:
                    dfs_recursivo(vecino)

        dfs_recursivo(nodo_inicial)

Nodos = ["A", "B", "C", "D", "E"]
aristas = [("A","B", 5),
        ("A","C", 6),
        ("B","D", 1),
        ("C","E", 3),
        ("E","D", 7)]
graph = Graph(Nodos, dirijido = True)

for v,u,p in aristas:
    graph.unir_nodos(v,u,p)

graph.imprimir_aristas()
grados = graph.grado()
for nodo,grado in grados.items():
    print(f"[{nodo}] ---> {grado}")
graph.Dijktra("B", "E")