#input
#6
# + 1
# ? 1
# + 200
# ? 2
# + 200
# ? 200

# result
# 1
# 0
# 2

q = int(input())
temp_list = []
counter = [0] * 201
for i in range(q):
    temp_list = input().split()
    if temp_list[0] == '+':
        counter[int(temp_list[1]) - 1] += 1
    elif temp_list[0] == '?':
        print(counter[int(temp_list[1]) - 1])

