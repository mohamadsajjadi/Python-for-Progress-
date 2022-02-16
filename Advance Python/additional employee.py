number = int(input())
lst = list()
for i in range(number):
    lst.append(input().split()[0])
max = 0
for item in lst:
    item_count = lst.count(item)
    if item_count > max:
        max = item_count
print(max)
