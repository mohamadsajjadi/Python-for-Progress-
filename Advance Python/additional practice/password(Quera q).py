# گاوصندوقی kk قفل چرخان دارد که روی هرکدام، ترتیبی از اعداد ۱ تا ۹ قرار دارد. زیر هر قفل چرخان یک نشان وجود دارد که به یکی از اعداد آن اشاره می‌کند و با چرخاندن قفل، این عدد تغییر می‌کند. حال یک عدد kk رقمی بعنوان رمز داده شده، حداقل تعداد چرخاندن چرخانه‌ها برای این که اعداد اشاره شده برابر عدد رمز باشد چقدر است؟
# test case

# 3
# 123
# 241356789
# 987546231
# 956874231

# result
# 7
k = int(input())
password = input()
sum = 0
for i in range(k):
    s = input()
    for j in range(len(s)):
        if s[j] == password[i]:
            absIndex = abs(j - len(s))
            if j < absIndex:
                sum += j
            else:
                sum += absIndex
print(sum)

