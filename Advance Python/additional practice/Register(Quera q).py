# حتماً دیده‌اید که در بخش عضویت بسیاری از وب‌سایت‌ها برای امنیت بیشتر محدودیت‌هایی بر روی نام کاربری و گذرواژه وجود دارد. می‌خواهیم با پایتون تابعی بنویسیم که تعدادی نام کاربری و گذرواژه دریافت کند و بر اساس قواعدی معتبر بودن آن‌ها را بررسی کند و در نهایت لیست نام‌های کاربری مجاز به عضویت را برگرداند.
#
# شرایط عضویت
# طول رمز عبور بزرگتر یا مساوی ۶ باشد.
# طول نام کاربری بزرگتر یا مساوی ۴ باشد.
# کسی مجاز به عضویت با نام‌های کاربری quera و codecup نیست.
# کاربری که رمز عبور او فقط از اعداد تشکیل شده‌ باشد مجاز به عضویت نیست.
# تابعی با نام check_registration_rules بنویسید که نام کاربری و گذرواژه‌ی تعدادی کاربر را مانند نمونه‌ی زیر دریافت کند و در خروجی لیستی از نام‌های کاربری مجاز به عضویت را برگرداند. ترتیب اعضای لیست خروجی اهمیت ندارد.

# testcase
# >>> check_registration_rules(username='password', sadegh='He3@lsa')
# ['username', 'sadegh']
def check_registration_rules(**kwargs):
    lst = list()
    for keys, values in kwargs.items():
        if keys != 'quera' and keys != 'codecup' and len(keys) >= 4 and len(values) >= 6 and not str(
                values).isnumeric():
            lst.append(keys)
    print(lst)


check_registration_rules(quera='qwerty80', mmdreza='monday80', ali="aliali@", mammad="salam")
