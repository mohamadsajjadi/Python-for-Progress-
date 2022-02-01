# input
# 5
# 1 2 1 3 4

# result
# 2


n = int(input())
my_list = [int(i) for i in input().split()]
counter = [0] * 101
minimum = 100
minimum_index = []
for member in my_list:
    counter[member] += 1

print(counter)
for index in range(1, 101):
    if counter[index] == 0:
        pass
    elif counter[index] < minimum:
        minimum = counter[index]
        minimum_index = index

print(minimum_index)
