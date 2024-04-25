
bandera = False
n = 0
nums = []
target = 0
n =int(input())
entrada = input()
nums = [int(entrada) for entrada in entrada.split()]
target = int(input())

for i in range(len(nums)):
        if bandera == True:
            break
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f'{i}, {j}')
                bandera = True
