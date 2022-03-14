# input
# 4 4
# 277 30 971 789
# 65 379 158 855
# 892 92 267 454
# 449 293 735 533
# 2 3
# 4 3
# 1 3
# 2 4

#result
#2719

n, m = map(int, input().split())
my_2D_list = [[int(j) for j in input().split()] for i in range(n)]
my_locate_list = [[int(j) for j in input().split()] for i in range(m)]

sum = 0
for i in range(m):
    sum += my_2D_list[my_locate_list[i][0] - 1][my_locate_list[i][1] - 1]
print(sum)
