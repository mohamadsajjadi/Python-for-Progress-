# input
# 4 4
# 1 2 10 13
# ? 3
# ? 5
# ? 1
# ? 10

# result
# 0
# 0
# 1
# 1


n, q = map(int, input().split())
my_list = [int(item) for item in input().split()]

for i in range(q):
    L = 0
    R = n
    s = list(input().split())
    while R - L > 1:
        mid = (L + R) // 2
        if my_list[mid] <= int(s[1]):
            L = mid
        elif my_list[mid] > int(s[1]):
            R = mid

    if my_list[L] == int(s[1]):
        print(1)
    else:
        print('0')

