import os
import re


def explore(ttype, address):
    ttype = '.' + ttype
    dic = dict()
    var = list(os.walk(address))
    for item in var:
        counter = 0
        for file in item[2]:
            if re.match(r".+" + ttype + "$", file):
                counter += 1
        if counter != 0:
            dic[item[0]] = counter
        else:
            continue
    print(dic)

os.path.r
explore('txt', "sample_test_media/A")
