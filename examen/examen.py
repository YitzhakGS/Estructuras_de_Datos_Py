from pila import Pila

P1 = Pila(4)
P2 = Pila(4)
re = Pila(5)
me_llevo = Pila(4)

registro1 = input()
for i in range(len(registro1)):
    P1.push(int(registro1[i]))

registro2 = input()
for i in range(len(registro2)):
    P2.push(int(registro2[i]))

def digitos(resul):
    if isinstance(resul, int) and 10 <= resul < 100:
        decenas = resul // 10
        unidades = resul % 10
        return decenas, unidades
    else:
        return None

def sumatoria(P1, P2, re, me_llevo):
    num1 = P1.peek()
    num2 = P2.peek()
    
    if not me_llevo.empty():
        num3 = me_llevo.peek()
        num2 += num3
    
    resul = num1 + num2
    suma = digitos(resul)
    
    if suma is None:
        re.push(resul)
    else:
        decenas, unidades = suma
        me_llevo.push(decenas)
        re.push(unidades)
    

def desplazar(P1, P2):
    P1.pop()
    P2.pop()

while not P1.empty():
    sumatoria(P1, P2, re, me_llevo)
    desplazar(P1, P2)

while not me_llevo.empty():
    ultimo = me_llevo.peek()
    re.push(ultimo)
    me_llevo.pop()

re.show()

