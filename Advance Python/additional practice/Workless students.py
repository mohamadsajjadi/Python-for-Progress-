# سلیب و فرهاد و سعید برای تمرین ریاضی،‌ بازی زیر را انجام می‌دهند.
# همزمان تست کیس را بخوانید تا بهتر متوجه شوید.
# سلیب یک معادله به صورت A + B = CA+B=C انتخاب می‌کند که در آن هر سه عدد نامنفی هستند. سپس معادله را در کاغذ می‌نویسد و آن را به فرهاد می‌دهد.
#
# بعد از آن فرهاد، از بین AA و BB و CC یک عدد و سپس xx رقم متوالی از همان عدد انتخاب کرده و بدون اینکه سعید ببیند به جای آن، یک # می‌گذارد (xx حداقل صفر و حداکثر به اندازه طول عدد انتخابی است).
#
# برای مثال فرهاد می‌تواند معادله 32 + 24 = 5632+24=56 را به \#2 + 24 = 56#2+24=56 یا 32 + 24 = \#32+24=# و یا مثال‌های دیگر تبدیل کند.
#
# حال نوبت به سعید می‌رسد که معادله اولیه را حدس بزند. از آنجایی که سلیب کمی بی‌سواد است ممکن است از ابتدا معادله را اشتباه نوشته باشد و در این صورت سعید باید بگوید که معادله از ابتدا اشتباه بوده است.
#
# حال ما به شما معادله دست‌کاری شده توسط فرهاد را می‌دهیم و شما باید به سعید کمک کنید تا بفهمد باید به جای # چه ارقامی قرار گیرد، یا اینکه بگویید معادله از اول غلط بوده است.
#
# شما باید تابعی به نام solve در فایل ans.py بنویسید که معادله‌ای به شکل A+B=CA+B=C را در قالب یک رشته که دقیقا یکی از اعداد آن حاوی # است به عنوان ورودی دریافت کند؛ اگر به جای #‌ می‌توانستیم عددی نامنفی قرار دهیم عدد مناسب را جایگزین عدد حاوی # در معادله اولیه کرده و معادله را بازگردانید، در غیر این صورت '-1' را بازگردانید.

# test case
#  solve("10# + 50 = 10052")
# result
# '10002 + 50 = 10052'

# solve("15 + 1#2 = 136")
# result
# '-1'
import re


def solve(arr):
    numbers = arr.split()
    sum_numbers = list(map(str, [numbers[0], numbers[2]]))
    result = numbers[4]

    if result.isdigit():
        result = int(result)
        if sum_numbers[0].isdigit():
            regex_number = str(result - int(sum_numbers[0]))
            unknown_number = sum_numbers[1]
            equation = f'{sum_numbers[0]} + {regex_number} = {result}'
        else:
            regex_number = str(result - int(sum_numbers[1]))
            unknown_number = sum_numbers[0]
            equation = f'{regex_number} + {sum_numbers[1]} = {result}'
    else:
        regex_number = str(int(sum_numbers[0]) + int(sum_numbers[1]))
        unknown_number = result
        equation = f'{sum_numbers[0]} + {sum_numbers[1]} = {regex_number}'

    if re.match('^[0-9]+#[0-9]+$', unknown_number):
        unknown_regex = re.findall(r'[0-9]+', unknown_number)
    elif re.match('^[0-9]+#$', unknown_number):
        unknown_regex = re.findall(r'[0-9]+', unknown_number)
        unknown_regex.append('')
    elif re.match('^#[0-9]+$', unknown_number):
        unknown_regex = re.findall(r'[0-9]+', unknown_number)
        unknown_regex.insert(0, '')
    else:
        unknown_regex = ['', '']

    regex = r'^' + unknown_regex[0] + r'[0-9]+' + unknown_regex[1] + r'$'

    if re.match(regex, regex_number):
        return equation
    else:
        return '-1'
