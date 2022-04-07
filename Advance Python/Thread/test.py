# در این سوال از شما می‌خواهیم یک decorator بنویسید که مانند کلید واژه synchronized در جاوا عمل کند.
#
# این دکوراتور باید به گونه‌ای باشه که اگر در بالای تابعی نوشته شد، ترد‌های مختلف نتوانند به صورت همزمان آن را صدا کنند؛ یعنی با استفاده از یک شی Lock باید کاری کند که در هر زمان فقط یک ترد درون تابع باشد و چند تردی که آن را صدا می‌کنند به ترتیب اجرا شوند.
from threading import Thread, Lock


def synchronized(f):
    lock = Lock()

    def inner_def(*args, **kwargs):
        lock.acquire()
        f(*args, **kwargs)
        lock.release()

    return inner_def


a = 0


@synchronized
def f():
    global a
    for i in range(300000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)

t.start()
s.start()

t.join()
s.join()
# for i in range(10):
#     f()
print(" **** ", a)
