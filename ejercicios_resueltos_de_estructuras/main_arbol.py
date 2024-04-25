
from arbol_binario import Arbol_Binario

tree = Arbol_Binario()

tree.agregar_nodo(15)
tree.agregar_nodo(10)
tree.agregar_nodo(23)
tree.agregar_nodo(11)
tree.agregar_nodo(13)
tree.agregar_nodo(25)
tree.agregar_nodo(43)
tree.agregar_nodo(18)
tree.agregar_nodo(30)

print(f"\nEl dato raiz del arbol es: {tree.root.dato}\n") #identificar raiz principal

nodos_hermanos = tree.hermanos(tree.root) #identificar nodos hermanos y altura
for nivel, nodos in nodos_hermanos.items():
    print(f"Nivel: {nivel}")
    print(f"    - {nodos}")
print("\n")

nodos_padre = tree.padres(tree.root) #identificar quien es padre de quien
for padre, nodos in nodos_padre.items():
    print(f"Padre:   {padre}")
    print(f"    - {nodos}")
print("\n")

tree.grado(tree.root) #identificar el grado de los nodos junto con las hojas




