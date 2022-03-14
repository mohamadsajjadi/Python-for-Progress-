x = \
    (
        {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
        {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
        {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
        {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}
    )


def fruits(fruit_list):
    dic = dict()
    for i in range(len(fruit_list)):
        main_list = list(fruit_list[i].values())
        if main_list[1] == "sphere" and 300 <= main_list[2] <= 600 and 100 <= main_list[3] <= 500:
            if main_list[1] in dic:
                dic[i] += 1
            else:
                dic.update({main_list[0]: 1})
    return dic


print(fruits(x))
