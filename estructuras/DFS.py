lista = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}
color = {}
parent = {}
trav_time = {}
dfs_trans_output = []

for node in lista.keys():
    color[node] = "w"
    parent[node] = None
    trav_time[node] = [-1, -1]

print(color)
print(parent)
print(trav_time)

time = 0


def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_trans_output.append(u)
    for v in lista[u]:
        if color[v] == "w":
            parent[v] = u
            print("parent", parent)
            dfs_util(v)

    color[u] = "B"
    trav_time[u][1] = time
    time = time + 1


dfs_util("A")
print(dfs_trans_output)
print(trav_time)
