k = int(input())
password = input()
sum = 0
for i in range(k):
    s = input()
    for j in range(len(s)):
        if s[j] == password[i]:
            absIndex = abs(j - len(s))
            if j < absIndex:
                sum += j
            else:
                sum += absIndex
print(sum)

