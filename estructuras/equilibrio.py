import pilas
import lista_enlazada
from pilas import Pila
from lista_enlazada import linkedList

formula = [str(entrada) for entrada in input("")]
contador = 0
pila = Pila()
pila_vacia = pila.is_empty()
lista = linkedList()
lista2 = linkedList()



def presedencia(caracter):
    if caracter == "*" or caracter == "/":
        return 2
    elif caracter == "+" or caracter == "-":
        return 1
    elif caracter == "^":
        return 3
    elif caracter == ")":
        return 0


for i in range(len(formula)):
    caracter = formula[i]
    if caracter == "(":
        contador += 1
        pila.push(caracter)
    elif caracter == ")":
        contador -= 1
        pila.pop()
    else:
        pass
    
    while i < len(formula):
        simbolo = formula[i]
        simbolo_tope = lista2.peek()
        if simbolo.isdigit():
            lista.add_at_end(simbolo)
        else:
            if simbolo == ")":
                while(True):
                    lista2.eliminar()
                    if simbolo_tope == ")" or lista2.is_empty():
                        break
                    lista.add_at_end(simbolo_tope)
            elif simbolo != "(":
                while(simbolo <= presedencia(simbolo_tope)):
                    lista2.eliminar()
                    lista.add_at_end(simbolo_tope)
            else:
                lista2.add_at_from(simbolo)
        while not pila_vacia:
            lista2.eliminar()
            lista.add_at_end(simbolo_tope)
    


lista.imprime()
    