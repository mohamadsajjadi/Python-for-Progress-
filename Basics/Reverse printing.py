# In this program
# we receives a number from the input at each step and continues to work until the digit zero is entered.
# After entering the zero digit, this program must print the entered numbers in reverse order.

my_list = []
while True:
    num = int(input())
    if num == 0:
        break
    my_list.append(num)
print(my_list[::-1])