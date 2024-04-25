
def seleccion(lista, valor_total, cantidad):
    for indice in range(cantidad):
        num1 = indice 
        x = valor_total - lista[indice]
        for sub_indice in range(indice + 1, cantidad):
            if lista[sub_indice] == x:
                num2 = sub_indice
                return num1, num2
    
    return None

#cuanto elemtos voy a ingresar 
n = int(input())
#inicializo la lista de cada elemeto
nums = []
#ingreso el costo de cada elemto a la lista
#la cadena se guarda enentrada y luego se itera entre cada elmento para separarlo 
entrada = input()
nums = [int(nums) for nums in entrada.split()]

#for elemntos in range(n):
#    costo = int(input())
#    nums.append(costo)
#ingreso el valor de la suma de los dos objetos 
target = int(input())

salida = seleccion(nums, target, n)

print(salida)







