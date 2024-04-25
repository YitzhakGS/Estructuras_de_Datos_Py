
n = int(input(''))
nums = [int(item) for item in input("").split()]
bandera = False
for i in range(len(nums)):
    if bandera == True:
        break
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            bandera = True
        else:
            bandera = False
            
if bandera == True:
    print('verdadero')
elif bandera == False:
    print('falso')
