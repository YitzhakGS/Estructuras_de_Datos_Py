adj_lista = {
    "A": ["B","C"],
    "B": ["A","D"],
    "C": ["A","E"],
    "D": ["B","E"],
    "E": ["C","D"],
}
adj_lista["A"].append("D")
adj_lista["D"].append("A")
print(adj_lista["A"])
print(adj_lista["D"])