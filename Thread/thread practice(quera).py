import functions
from threading import Thread


def sol(func):
    thread = []
    for i in range(len(func)):
        thread.append(Thread(name=str(i + 1), target=func[i]))
    for item in thread:
        item.start()
    for item in thread:
        item.join()


def solve():
    sol(functions.f)
    sol(functions.g)
    sol(functions.h)
