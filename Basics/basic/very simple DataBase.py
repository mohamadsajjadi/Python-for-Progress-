# input
# 7
# + 1 1   it means replace temp_list[2] (1) to my_list[1](1)
# + 2 3   it means replace temp_list[2] (3) to my_list[1] (2)
# + 2 10
# + 4 5
# + 2 100
# - 2
# - 2

# result
# 1
# 1 3
# 1 10 3
# 1 10 3 5
# 1 100 10 3 5
# 1 10 3 5
# 1 3 5


def print_my_list(list_1):
    if not list_1:
        print('EMPTY')
    else:
        for var in list_1:
            print(var, end=' ')
        print()


number = int(input())
my_list = []
temp_list = []
for i in range(1, number + 1):
    temp_list = input().split()
    if temp_list[0] == '+':
        my_list.insert(int(temp_list[1]) - 1, (temp_list[2]))
        print_my_list(my_list)
    elif temp_list[0] == '-':
        my_list.pop(int(temp_list[1]) - 1)
        print_my_list(my_list)
    temp_list.clear()
