# ما از شما می‌خواهیم که یک decorator به اسم decorator‍ تعریف کنید که با استفاده از یک تابع کمکی، تابع اصلی را اجرا کند و اگر ورودی‌ها معتبر نبودند عبارت error را برگرداند.
#
# این دکوراتور یک تابع validator‍ را به عنوان ورودی می‌گیرد و قبل از صداکردن تابعی که قرار است به decorator داده‌ شود؛ با توجه به تابع ‍‍validator بررسی می‌کنید ورودی‌ها معتبر هستند یا نه.
#
# نحوه کار validator به این شکل است که اگر مقدار true برگرداند یعنی ورودی‌ها معتبر هستند و در غیر این صورت نامعتبرند.
#
# حال اگر ‍ورودی‌ها معتبر بودند، باید مقدار خروجی تابع و در غیر این صورت error برگردانده شود.

# test case with result

# def validator(x):
#     return x>=0
#
# @decorator(validator)
# def f(x):
#     return x**0.5
#
# -> print(f(4)) #should print 2.0
# -> print(f(-4)) #should print error
def decorator(validator):
    def higher_function(func):
        def inner_function(*args):
            if validator(*args):
                result = func(*args)
                return result
            else:
                return "error"

        return inner_function

    return higher_function
