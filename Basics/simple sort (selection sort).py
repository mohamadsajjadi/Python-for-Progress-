# simple sort
# sort and reverse it!

# input
# 4
# 7 8 4 1

# result
# 8 7 4 1
def swap(lst1, index_1, index_2):
    temp = lst1[index_1]
    lst1[index_1] = lst1[index_2]
    lst1[index_2] = temp
    return lst1


n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    min = i
    for j in range(i, n):
        if lst[min] > lst[j]:
            min = j
    swap(lst, i, min)

lst = lst[::-1]
for item in lst:
    print(item, end=' ')

