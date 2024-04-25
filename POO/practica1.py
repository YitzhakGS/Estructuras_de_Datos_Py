class Coche: #Nombre de la clase
    
    ruedas = 4
#constructor
    def __init__(self, color, aceleracion): #Constructor de la clase 
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
#Metodos 
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
        
    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v 
        
#objetos a base de los constructores (clases)
c1 = Coche('rojo', 20)
print(c1.color)
print(c1.aceleracion)
#se cambia un atribujo de un objeto ya definido
c1.color = 'azul'
print(c1.color)
print(c1.aceleracion)