Number = int(input())
myList = [] * Number
count_save = [0] * 101

myList = list(map(int, input().split()))  # 5 2 3 4 5
for item in myList:
    count_save[item] = myList.count(item)

count_save_min = min(x for x in count_save if x != 0)
print(count_save.index(count_save_min))
