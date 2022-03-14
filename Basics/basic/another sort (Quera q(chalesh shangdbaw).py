# input
# 7
# Add 10
# Add 2
# Ask 1
# Ask 2
# Add 5
# Ask 2
# Ask 3

# result
# 2
# 10
# 5
# 10

q = int(input())
input_list = []
main_list = []
for i in range(q):
    input_list = input().split()
    # print(input_list[0], input_list[1])
    # print(type(input_list[0]))
    if input_list[0] == "Add":
        main_list.append(int(input_list[1]))
        main_list = sorted(main_list)
        # print(main_list)
    elif input_list[0] == "Ask":
        print(main_list[int(input_list[1]) - 1])

