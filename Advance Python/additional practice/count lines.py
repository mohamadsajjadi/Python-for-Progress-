def solve(path):
    path1 = open(path, 'r')
    lst = list()
    counter = 0
    for lines in path1:
        lst.append(lines.strip())
    for item in lst:
        if not item.startswith('#') and item != '':
            counter += 1
    return counter


path = open('info.txt', 'r')
print(solve(path))

