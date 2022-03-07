# lst = [["pers", 1, 2], ["sep", 3, 4], ["esteg", 3, 4], ["pir", 10, 1]]
# print(sorted(lst, key=lambda l: l[2]))


def swap(lst1, index_1, index_2):
    temp = lst1[index_1]
    lst1[index_1] = lst1[index_2]
    lst1[index_2] = temp
    return lst1


def sort_team():
    sorted_list = [[1, 4, 2], [1, 4, 1], [1, 2, 3], [1, 2, 5]]

    for i in range(len(sorted_list)):
        min = sorted_list[i][1]
        min_index = i
        min_lost = sorted_list[i][2]
        for j in range(i, len(sorted_list)):
            if min > sorted_list[j][1]:
                min = sorted_list[j][1]
                min_lost = sorted_list[j][2]
                min_index = j
            elif min == sorted_list[j][1]:
                if min_lost < sorted_list[j][2]:
                    min = sorted_list[j][1]
                    min_lost = sorted_list[j][2]
                    min_index = j
        swap(sorted_list, i, min_index)

    lst = sorted_list[::-1]
    for item in lst:
        print(item, end=' ')


sort_team()
