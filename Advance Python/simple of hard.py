lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(*sorted(dict.fromkeys(x for x in map(int, input().split()[5::6]) if x % 6 == 0)))
