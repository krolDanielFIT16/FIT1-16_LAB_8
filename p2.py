import random
import numpy as np

m = int(input("m = "))
n = int(input("n = "))

A = np.empty((m, n))
B = np.empty((m, n))

for i in range(m):
    for j in range(n):
        A[i][j] = random.randint(1, 50)
        B[i][j] = random.randint(1, 50)

print(f"{A+B=}")
print(f"{A*B=}")
print(f"{A-B=}")
