s = input()
s = s.strip('=')
sLength = len(s)
main_list = []
for i in range(sLength):
    if s[i] != '=':
        main_list.append(s[i])
    else:
        main_list.pop()
for item in main_list:
    print(item, end='')
