# محمد یک لیست nn تایی از اعداد دارد و در گروه‌های مختلف آن را تقسیم‌بندی می‌کند؛ به این صورت که mm عضو اول را در یگ گروه قرار می‌دهد، mm عضو بعدی را در یک گروه و به همین ترتیب اعضا را گروه بندی می‌کند (دقت کنید که گروه آخر ممکن است کمتر از mm عضو داشته باشد).
#
# محمد از روی این اعداد، یک لیست جدید می‌سازد که عضو iiام آن، جمع اعضای گروه iiام باشد.
#
# او که به شطرنج علاقه خاصی دارد به صورت یکی در میان اعضای لیست جدید را از هم کم و زیاد می‌کند؛ به این معنا که از عضو اول لیست جدید، عضو دوم را کم می‌کند و سپس عضو سوم را اضافه می‌کند و از این مقدار عضو چهارم را کم می‌کند و این روند را ادامه می‌دهد تا به آخر لیست جدید برسد و سپس مقدار نهایی را به عنوان ارزش لیست در نظر می‌گیرد.
# شما باید تابع ‍‍calculator(n, m, ls) را پیاده‌سازی کنید که به ترتیب nn (تعداد اعضای لیست)، mm (تعداد اعضای هر گروه) و lsls (خود لیست) را ورودی بگیرد و ارزش نهایی لیست را بر‌گرداند.
def calculator(n, m, ls):
    if m == 1:
        return simple_calculations(ls)
    else:
        return complicated_calculation(m, ls)


def simple_calculations(ls):
    sum = 0
    for i in range(0, len(ls), 2):
        sum += ls[i]
    sum_2 = 0
    for j in range(1, len(ls), 2):
        sum_2 += ls[j]
    result = sum - sum_2
    return result


def complicated_calculation(m, ls):
    my_list = []
    first_list = ls[:m]
    my_list.append(first_list)
    for i in range(m, len(ls)):
        if i % m == 0:
            lst = ls[i:i + m]
            my_list.append(lst)
    last_list = []
    for item in my_list:
        last_list.append(sum(item))
    return simple_calculations(last_list)


print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
