class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0


    def validacion(self, cadena):
        pila2 = Pila()
        con = 0
        for i in range(len(cadena)):
            if cadena[i] in "({[":
                pila2.push(cadena[i])
                con += 1
            elif cadena[i] in ")}]":
                if pila2.isEmpty():
                    print("Esta desbalanceada")
                    return
                top = pila2.pop()
                if (top == "{" and cadena[i] != "}") or \
                    (top == "[" and cadena[i] != "]") or \
                    (top == "(" and cadena[i] != ")"):
                    print("Esta desbalanceada")
                    return
                con -= 1

        if con == 0:
            print("Esta balanceada")
            self.convertirExpresion(cadena)
        else:
            print("Esta desbalanceada")

    def convertirExpresion(self, cadena):
        stack = Pila()
        expPosfija = []
        for i in range(len(cadena)):
            caracter = cadena[i]
            if caracter.isdigit():
                expPosfija.append(caracter)
            else:
                if caracter == ")":
                    while stack.peek() != "(" and not stack.isEmpty():
                        expPosfija.append(stack.pop())
                    stack.pop()  
                elif caracter in "+-*/":
                    while (not stack.isEmpty() and
                            precedencia(caracter) <= precedencia(stack.peek())):
                        expPosfija.append(stack.pop())
                    stack.push(caracter)
                else:
                    stack.push(caracter)

        while not stack.isEmpty():
            expPosfija.append(stack.pop())

        print("", ''.join(expPosfija))

def precedencia(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    return 0