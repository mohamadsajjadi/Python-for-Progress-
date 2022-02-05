# input
# 4
# zahra
# 2 19.6 17
# 1 tennis
# fariba
# 3 18 16 15
# 2 handball volleyball
# parisa
# 2 12 11
# 3 basketball swimming handball
# anahita
# 4 20 20 20 20
# 0

# result
# anahita
# zahra
# fariba
# parisa


def swap(lst1, index_1, index_2):
    temp = lst1[index_1]
    lst1[index_1] = lst1[index_2]
    lst1[index_2] = temp
    return lst1


def my_sort(list):
    for i in range(n):
        min = i
        for j in range(i, n):
            if list[min][1] > list[j][1]:
                min = j
            elif list[min][1] == list[j][1]:
                if list[min][2] > list[j][2]:
                    min = j
                elif list[min][2] == list[j][2]:
                    if list[min][3] < list[j][3]:
                        min = j
        swap(list, i, min)


n = int(input())
main_list = []
for i in range(n):
    my_list = []
    my_list.append(input())
    my_input = list(map(float, input().split()))
    average = 0
    length = int(my_input[0]) + 1
    for j in range(1, length):
        average += my_input[j]
    average = average // my_input[0]
    my_list.append(average)
    l = int(input().split()[0])
    my_list.append(l)
    my_list.append(i)
    main_list.append(my_list)  # 2D
my_sort(main_list)
for i in range(n):
    print(main_list[n - i - 1][0])

