# in this program,we want to calculate number's factorial
n = int(input())
sum = 1
for i in range(1, n + 1):
    sum *= i
print(sum)
