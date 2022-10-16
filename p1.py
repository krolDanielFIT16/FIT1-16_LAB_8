import random
from array import *

a = int(input("a = "))
b = int(input("b = "))

arr = array("i", [])

for i in range(12):
    arr.append(random.randint(a, b))

arr = array("i", sorted(arr))
print(arr)
