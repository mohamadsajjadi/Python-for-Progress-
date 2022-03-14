# input
# 5 5
# quera
# users
# enjoy
# round
# award

# result
# 2

n, m = map(int, input().split())
myList = [[item for item in input()] for i in range(n)]
s = input()
counter = 0
for i in range(n):
    for j in range(m - len(s) + 1):
        flag = True
        for k in range(len(s)):
            if not myList[i][j + k] == s[k]:
                flag = False
        if flag is True:
            counter += 1

for i in range(m):
    for j in range(n - len(s) + 1):
        flag = True
        for k in range(len(s)):
            if not myList[j + k][i] == s[k]:
                flag = False
        if flag is True:
            counter += 1
