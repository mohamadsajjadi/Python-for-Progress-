# از شما می‌خواهیم تابعی به نام explore بنویسید که با گرفتن آدرس نسبی یک پوشه و یک پسوند، تعداد فایل‌هایی که با آن پسوند، در آن پوشه و زیرپوشه‌هایش قرار دارد را به همراه آدرس نسبی آن پوشه‌ها در قالب یک لغت‌نامه برگرداند.
#
# یعنی خروجی تابع باید یک لغت‌نامه باشد که هر کلید آن آدرس یک پوشه (با آدرس‌دهی از پوشه‌ای که فایل پایتون در آن قرار دارد) و هر مقدار آن تعداد فایل‌هایی است که با آن پسوند به طور مستقیم در آن پوشه قرار دارند. اگر پوشه‌ای شامل فایل مورد نظر ما نبود نباید در لغت‌نامه باشد.
import os
import re


def explore(ttype, address):
    ttype = '.' + ttype
    ttype = ttype.lower()
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

    explore('txt', "sample_test_media/A")
