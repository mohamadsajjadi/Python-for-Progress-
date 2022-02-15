from statistics import *


def calc(a):
    return sum(a) / len(a), median(a), max(a)


lst = [4, 5, 20]
print(calc(lst))
