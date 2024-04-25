temperatura = []

total_valores = input('cuantos valores va a ingresar? ')
temp_max = 0.0
for valores in range (int(total_valores)):
    temp = input()
    temperatura.append(float(temp))

for temp in range(len(temperatura)):
    if temperatura[temp] > temp_max:
        temp_max = temperatura[temp]

print(f'la temperatura maxima es: {temp_max}')