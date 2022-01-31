n, m = map(int, input().split())
# first_list = [] * n
# second_list = [] * n
first_list = [[int(item) for item in input().split()] for i in range(n)]
second_list = [[int(item) for item in input().split()] for j in range(n)]
final_list = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        final_list[i][j] = first_list[i][j] + second_list[i][j]
for i in range(n):
    for j in range(m):
        print(final_list[i][j], end=' ')
    print()
