#input
# 5 3
# 1 2 3 4 5


#result
# 0 to 2
# 1 to 3
# 2 to 4


n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, n):
    flag = True
    if i + k - 1 < n:
        for j in range(1,k+1):
            if a[j] < a[j - 1]:
                flag = False
    else:
        flag = False
    if flag:
        print("{} to {}".format(i, i + k - 1))
