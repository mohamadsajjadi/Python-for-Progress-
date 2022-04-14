def get_func(my_list):
    my_dic = {
        "age": lambda x: f"Ali is {x} years old",
        "name": lambda x: f"My name is {x}",
        "live": lambda x: "he is alive" if x else "he is dead"
    }
    return [my_dic.get(func) for func in my_dic]


ls = get_func(['age', 'name', 'live'])

print(ls[0](13))
print(ls[1]('Sadegh'))
print(ls[2](True))
print(ls[2](False))
