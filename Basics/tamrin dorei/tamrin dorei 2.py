def calculator(n, m, ls):
    if m == 1:
        return simple_calculations(ls)
    else:
        return complicated_calculation(m, ls)


def simple_calculations(ls):
    sum = 0
    for i in range(0, len(ls), 2):
        sum += ls[i]
    sum_2 = 0
    for j in range(1, len(ls), 2):
        sum_2 += ls[j]
    result = sum - sum_2
    return result


def complicated_calculation(m, ls):
    my_list = []
    first_list = ls[:m]
    my_list.append(first_list)
    for i in range(m, len(ls)):
        if i % m == 0:
            lst = ls[i:i + m]
            my_list.append(lst)
    last_list = []
    for item in my_list:
        last_list.append(sum(item))
    return simple_calculations(last_list)


print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
