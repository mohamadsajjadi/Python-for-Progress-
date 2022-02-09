my_list = []
while True:
    inp = int(input())
    if inp == 0:
        for i in reversed(my_list):
            print(i)
        break
    else:
        my_list.append(inp)
