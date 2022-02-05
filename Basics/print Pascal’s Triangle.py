# input
# 5

# result
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

from math import factorial

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()
