# input
# hamidvaomidvaamid
# mid

# result
# 3 9 15

s = input()
p = input()
for char in range(len(s)):
    flag = True
    for index in range(len(p)):
        if char + index <= len(s):
            if not s[char + index] == p[index]:
                flag = False
        else:
            flag = False
    if flag is True:
        print(char + 1, end=" ")
