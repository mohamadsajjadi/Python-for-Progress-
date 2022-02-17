def process(path):
    with open(path, 'r') as account_file:
        lst = list()
        for row in account_file.readlines():
            lst.append(list(map(int, row.rstrip().split(','))))
        print(lst)
    with open('ans.csv', 'w') as csv_file:
        for i in range(len(lst)):
            sum = 0
            for j in range(len(lst[i])):
                sum += lst[i][j]
            lst[i].append(sum)
        answer = ''
        for item in lst:
            answer += str(item[0])
            for index in item[1:]:
                answer += ", " + str(index)
            answer += '\n'
        csv_file.write(answer)


process('test1_sample.csv')
