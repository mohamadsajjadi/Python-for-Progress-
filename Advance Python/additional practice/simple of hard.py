# به شما یک آرایه از اعداد داده می‌شود. ما به یک عدد رهنمایی می‌گوییم اگر هم خودش بر ۶ بخش پذیر باشد و هم شماره‌ی جایگاهی که در آرایه ظاهر شده است بر ۶ بخش پذیر باشد
# test case
# 1 2 3 4 5 6 7 8 9 10 11 12
# result
# 6 12


# 3 4 1 37 21 18 23 25 27 22 43 26
# 18

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(*sorted(set(x for x in map(int, input().split()[5::6]) if x % 6 == 0)))
