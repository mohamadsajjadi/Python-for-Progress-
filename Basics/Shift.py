# We have a number that are in sequence
# each series we want to bring the last element to the first and print the numbers.
# To do this, we use an array.

n, x = map(int, input().split())
my_list = [0] * n
my_list = [int(member) for member in input().split()]
second_list = my_list[-x:]
third_list = my_list[0:-x]
for index in third_list:
    second_list.append(index)
for index in second_list:
    print(index, end=' ')
