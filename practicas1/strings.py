cadena1 = input()
print(cadena1)
posicion = cadena1.find("*")
print(posicion)#es entero

#separo la cadena con espacios
cadena_con_espacios = ' '.join(cadena1)
print(cadena_con_espacios)
#ya con la cadena separada convierto a 0 los "."
cadena2 = [int(0) if item == "." else item for item in cadena1]
print(cadena2)

for i in range(len(cadena2)):
    if cadena2[i] != '*':
        cadena2[i] += 1
#vuelvo a unir los caracteres en un texto
cadena_final = ''.join(map(str, cadena2))
print(cadena_final)