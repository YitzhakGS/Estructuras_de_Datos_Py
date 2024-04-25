import math
import heapq

class grafos:
    def __init__(self, Nodes, isdirected=False):
        self.nodes = Nodes
        self.adj_list = {}
        self.isdirected = isdirected
        for node in self.nodes:
            self.adj_list[node] = {}

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "-->", self.adj_list[node])

    def add_edge(self, u, v, w): 
        self.adj_list[u][v] = w
        if not self.isdirected:
            self.adj_list[v][u] = w

    def grades(self, node):
        return len(self.adj_list[node])

    def dijkstra(self, start, end):
        visited = {node: math.inf for node in self.nodes}
        prev = {node: None for node in self.nodes}
        visited[start] = 0
        queue = [(0, start)]
        while queue:
            current_dist, current_node = heapq.heappop(queue)
            if current_dist != visited[current_node]:
                continue
            for neighbour, weight in self.adj_list[current_node].items():
                distance = current_dist + weight
                if distance < visited[neighbour]:
                    visited[neighbour] = distance
                    prev[neighbour] = current_node
                    heapq.heappush(queue, (distance, neighbour))
        if visited[end] == math.inf:
            return None
        path = []
        while end is not None:
            path.append(end)
            end = prev[end]
        path.reverse()
        return path

nodes=["A","B","C","D","E"]
grafo=grafos(nodes, isdirected=False)
grafo.add_edge("A","B", 1)
grafo.add_edge("A","C", 3)
grafo.add_edge("B","D", 2)
grafo.add_edge("C","D", 5)
grafo.add_edge("C","E", 4)
grafo.add_edge("D","E", 1)

grafo.print_adj_list()

for node in grafo.nodes:
    print(f"El nodo {node} tiene grado {grafo.grades(node)}")

path = grafo.dijkstra("B", "C")
if path is not None:
    print("El camino más corto es:", path)
else:
    print("No hay camino")
