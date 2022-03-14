# input
# 11 1
# amirali
# ghasem
# majid
# mohammad
# ali
# golmohammad
# goli
# peyman
# gholi
# ahoora
# asghar

# result
# 4


n, k = map(int, input().split())
list = []
for i in range(11):
    list.append(input())
list = sorted(list)
max = 0
for i in range(n):
    counter = 0
    for j in range(i, n):
        if list[i][:k] == list[j][:k]:
            counter += 1
    if counter > max:
        max = counter
print(max)

