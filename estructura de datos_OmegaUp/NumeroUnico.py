
n = int(input(''))
nums = [int(item) for item in input("").split()]
num_U = 0
repetido = 0
for i in range(len(nums)):
    num_U = nums[i]
    contador = 1
    for j in range(i + 1, len(nums)):
        if num_U == nums[j] or num_U == repetido:
            contador += 1
            repetido = num_U
    if contador == 1:
        print(f'{num_U}')
        break