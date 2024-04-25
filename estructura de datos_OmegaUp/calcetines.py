
from collections import Counter

n = int(input())
nums = [int(item) for item in input("").split()]
contador = Counter(nums)

parejas = sum(count // 2 for count in contador.values())

print(parejas)