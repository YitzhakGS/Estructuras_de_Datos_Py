
def busqueda_binaria(num,lista):
    izq = 0
    der = len(lista)-1
    while izq <= der:
        medio = (izq + der)//2
        if num == lista[medio]:
            return medio
        elif num > lista[medio]:
            izq = medio + 1
        else:
            der = medio - 1
    return None
    

def buscar(num,lista):
    medio = busqueda_binaria(num,lista)
    if medio == None:
        print("el numero no se encuentra")
    else:
        print(f"el numero esta en la posiscion {medio}")

num = int(input("que valor desea buscar: "))
lista = [5,10,15,20,25,30]
buscar(num, lista)