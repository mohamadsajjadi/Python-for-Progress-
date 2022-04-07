# در این سوال برای ساده‌تر کردن مدیریت خطاها و مرتب کردن استثنا‌ها می‌خواهیم تمام خطاهایی که رخ می‌دهد را با یک قرارداد واحد در کلاسی به نام ExceptionProxy ذخیره کنیم. برای این کار به ازای هر خطایی که رخ می‌دهد، یک شی از کلاس ExceptionProxy می‌سازیم. با فرض اینکه e یک شی از کلاس ExceptionProxy است، کلاس ExceptionProxy دارای دو خصوصیت است.
#
# متن استثنای رخ داده‌ که از طریق e.msg قابل دسترس است.
# تابعی که باعث ایجاد استثنا شده که توسط e.function قابل دسترس می‌باشد.
# نحوه عملکرد
# از شما می‌خواهیم تابعی به نام transform_exceptions() بنویسید که یک لیست از توابع ورودی می‌گیرد. سپس هر کدام از توابع را صدا می‌کند (توابع بدون آرگومان هستند) و استثناهایی که رخ می‌دهد را با قرارداد بالا به شی‌ای از ExceptionProxy تبدیل کرده و در نهایت لیست خطا‌های تبدیل شده را به همان ترتیب توابع برگرداند. دقت کنید که اگر تابعی بدون خطا اجرا شد، باید یک شی ExceptionProxy ساخته و مقدار msg آنرا با "ok!" مقدار دهی کنید.

class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    lst = list()
    for item in func_ls:
        try:
            item()
            e = ExceptionProxy(msg='ok!', function=item)
            lst.append(e)
        except Exception as ex:
            e = ExceptionProxy(msg=str(ex), function=item)
            lst.append(e)
    return lst


def f():
    print(1 / 0)


def g():
    pass


tr_ls = transform_exceptions([f, g])

for exception in tr_ls:
    print("msg: " + exception.msg + "\nfunction name: " + exception.function.__name__   )
