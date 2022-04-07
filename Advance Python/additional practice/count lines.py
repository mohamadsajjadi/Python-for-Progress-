# از شما می‌خواهیم تابعی بنویسید که با گرفتن آدرس نسبی یک برنامه پایتون، تعداد خطوطی از آن که دارای دستور هستند را تشخیص دهد.
# test case
# a = input()
#
# b = int(a)
# print(b * b, a + a)
#   #if a = 3 output is 33.
# result
# 3
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
