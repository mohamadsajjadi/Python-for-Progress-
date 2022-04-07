# در این سوال باید برنامه‌ای بنویسد که یک فایل csv را بخواند، در آن تغییراتی انجام دهد و در نهایت فایل csv تغییر یافته خود را خروجی بدهد. نحوه کار با csv در انتهای سوال توضیح داده شده است.
#
# فایل csv که باید به عنوان ورودی برنامه شما آن را بخواند شامل یک جدول n×m می‌باشد که در هر خانه‌ی آن یک عدد صحیح وجود دارد.
#
# شما باید یک ستون جدید به انتهای این فایل csv اضافه کرده و در هر خانه‌ی آن جمع اعداد خانه‌هایی که در سطر این خانه قرار دارد را قرار دهید.
#
# برنامه شما باید تنها شامل یک تابع به نام process باشد که به عنوان ورودی آدرس فایل csv اولیه را می‌گیرد و به عنوان خروجی یک فایل csv جدید را در ans.csv ذخیره می‌کند.

# test case
# 3, 3, 1, 1, 1, 1, 1
# 1, 1, 4, 5, 6, 7, 8
# 1, 5, 6, 7, 4, 3, 1

# result
# 3, 3, 1, 1, 1, 1, 1, 11
# 1, 1, 4, 5, 6, 7, 8, 32
# 1, 5, 6, 7, 4, 3, 1, 27
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
