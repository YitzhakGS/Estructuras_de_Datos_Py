import pilas
import lista_enlazada
from pilas import Pila
from lista_enlazada import linkedList

formula = input("Ingrese la expresión infija: ")
contador = 0
pila = Pila()
lista = linkedList()

def presedencia(caracter):
    if caracter == "*" or caracter == "/":
        return 2
    elif caracter == "+" or caracter == "-":
        return 1
    elif caracter == "^":
        return 3
    elif caracter == ")":
        return 0

for caracter in formula:
    if caracter == "(":
        contador += 1
        pila.push(caracter)
    elif caracter == ")":
        contador -= 1
        while not pila.is_empty():
            simbolo_tope = pila.pop()
            if simbolo_tope == "(":
                break
            lista.add_at_end(simbolo_tope)
    elif caracter.isdigit():
        lista.add_at_end(caracter)
    else:
        while not pila.is_empty() and presedencia(caracter) <= presedencia(pila.peek()):
            simbolo_tope = pila.pop()
            lista.add_at_end(simbolo_tope)
        pila.push(caracter)

while not pila.is_empty():
    simbolo_tope = pila.pop()
    lista.add_at_end(simbolo_tope)

if contador == 0:
    print("La fórmula está bien balanceada")
else:
    print("La fórmula está mal balanceada")

lista.imprime()
