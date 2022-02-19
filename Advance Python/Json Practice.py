import json

var = dict()
n = int(input())
for i in range(n):
    data = input()
    if ":=" in data:
        key, value = data.split(' := ')
        var[key] = json.loads(value)
    else:
        data = data.split()
        index = data[1]
        index_first = index.index('[')
        index_end = index.index(']')
        index_digit = index[index_first + 1: index_end]
        key = index[:index_first]
        if index_digit.isdigit():
            print(var[key][int(index_digit)])
        else:
            index_digit = index_digit[1:-1]   # get only digit
            print(var[key][index_digit])
