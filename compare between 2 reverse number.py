a = int(input())
aInput = a
sum = 0
while a > 1:
    sum = (sum * 10) + int(a % 10)
    a /= 10

b = int(input())
bInput = b
sumB = 0
while b > 1:
    sumB = (sumB * 10) + int(b % 10)
    b /= 10

if sum < sumB:
    print(f"{aInput} < {bInput}")
elif sumB < sum:
    print(f"{bInput} < {aInput}")
else:
    print(f"{aInput} = {bInput}")