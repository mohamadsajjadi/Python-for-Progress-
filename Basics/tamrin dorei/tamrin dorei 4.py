x = \
    (
        {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
        {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
        {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
        {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}
    )


def fruits(fruit_list):
    main_list = []
    for dic in fruit_list:
        lst = list()
        for item in dic.values():
            lst.append(item)
        main_list.append(lst)
    print(main_list)

    my_dict = dict()
    for i in range(len(main_list)):
        if main_list[i][1] == "sphere" and 300 <= main_list[i][2] <= 600 and 100 <= main_list[i][3] <= 500:
            if main_list[i][0] in my_dict.keys():
                my_dict[main_list[i][0]] += 1
            else:
                my_dict[main_list[i][0]] = 1
    return my_dict


print(fruits(x))

# my_dic = dict()
# my_dic["ali"] += 1
# print(my_dic)
