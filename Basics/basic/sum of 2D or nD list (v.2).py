n, m = map(int, input().split())

firstList = [] * n
secondList = [] * n

firstList = [[item for item in input().split()] for i in range(n)]
secondList = [[index for index in input().split()] for i in range(n)]

finalList = [] * n
for index in range(n):
    col = []
    for member in range(m):
        col.append(int(firstList[index][member]) + int(secondList[index][member]))
    finalList.append(col)

for item in finalList:
    for member in item:
        print(member, end=' ')
    print()