# علیش که جدیدا نمی‌تونه خوب بنویسه، از پاشا می‌خواد که جمله‌ای که تو ذهنش هست رو واسش بنویسه. پاشا هم که می‌خواد استیل بیاد تصمیم می‌گیره که این جمله رو تایپ کنه اما از اون‌جایی که حتی بلد نیست تایپ کنه، وقتی داره جمله رو می‌نویسه به‌جای دکمه بک‌اسپیس (پاک کردن آخرین حرف نوشته شده در صورتی که وجود داشته باشد) دکمه = رو می‌زنه. پاشا هم که نمی‌خواد زحماتش حروم بشه و جلوی علیش ضایع بشه از شما کمک می‌خواد و به شما رشته‌ای که تایپ کرده رو میده و ازتون می‌خواد براش رشته اصلی رو بنویسید.
# test case

# sall=am
# result
# salam

# testtwoo===wo
# testtwo
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
