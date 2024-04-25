#algoritmo de ordenamiento por burbuja 

arrey = [5, 1, 10, 11, 7, 4, 2, 3, 8]
#se repite el recorrido del arreglo tantas veces sea el numero de elementos que contiene
for i in range(len(arrey)):
#se rcorre el arreglo hasta el penultima numero del arreglo ya que este ya estara ordenado
    for j in range(len(arrey)-1):
#si el numero donde encunatra el indice es mayor al num adyacente entonces intercambian lugares
        if (arrey[j] > arrey[j+1]):
#se es asi se realiza el cambio de varible usando una temporal para que no se pierda uno de los valores
            temp = arrey[j]
            arrey[j] = arrey[j+1]
            arrey[j+1] = temp
#se imprime la lista de los valores ordenados de menor a mayor 
print(arrey)