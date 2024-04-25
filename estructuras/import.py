import pilas
import dequ
import lista_enlazada
from pilas import Pila
from dequ import deq
from lista_enlazada import linkedList

lista = ["(","[","{","}","]",")"]
cadena = ["(", "[", "{"]

def string(lista, cadena):
    s = Pila()
    for i in lista:
        if i in cadena:
            s.push(i)
            
    for _ in range(3):
        s.peek()
        s.pop()

string(lista, cadena)






