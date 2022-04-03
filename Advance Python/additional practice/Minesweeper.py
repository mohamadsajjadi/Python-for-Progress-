def check_pos(x, y, m, n):
    pos = [-1, 0, 1]
    if maps[x][y] != '*':
        for i in pos:
            for j in pos:
                if i != 0 or j != 0:
                    if (0 <= x + i < m) and (0 <= y + j < n):
                        if maps[x + i][y + j] == '*':
                            maps[x][y] += 1
    return maps


def print_list(my_list):
    for item in my_list:
        print(*item)


m, n = map(int, input().split())
k = int(input())
maps = []
for i in range(m):
    maps.append([])
    for j in range(n):
        maps[i].append(0)

for i in range(k):
    bombLocation = input().split()
    maps[int(bombLocation[0]) - 1][int(bombLocation[1]) - 1] = '*'

for i in range(0, m):
    for j in range(0, n):
        check_pos(i, j, m, n)
print_list(maps)
