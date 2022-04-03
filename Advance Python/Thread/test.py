import threading
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
