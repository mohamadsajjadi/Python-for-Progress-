def f(x):
    if x % 2 == 0:
        return True
    else:
        return False


my_list = [1, 2, 3, 4, 8, 5, 4, 9, 10]

for item in filter(f, my_list):
    print(item, end=" ")
