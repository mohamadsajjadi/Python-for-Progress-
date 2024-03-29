# یک شناسه‌ی فرستنده نامعتبر است اگر فقط از عدد تشکیل شده باشد.
#
# محتوای پیام نامعتبر است اگر تعداد کاراکترهای غیرحرف، غیرعدد و غیرفاصله‌ بیش از نصف طول پیام باشد و در آن حداقل یک بار زیررشته‌ی spam (با هر ترکیبی از حروف کوچک و بزرگ انگلیسی) تکرار شده باشد.
#
# حال پیام‌ها از نظر معتبربودن یا نبودن و بدنه، در چهار دسته‌ زیر طبقه‌بندی می‌شوند. شما باید بسته به این که پیام در چه دسته‌ای قرار دارد،‌ عبارت خواسته شده را چاپ کنید.
#
# دسته‌ی Not Spam
# پیام‌هایی که شناسه و پیام بدنه معتبری دارند،. اگر پیام از این دسته بود عبارت Not Spam را چاپ کنید.
#
# دسته‌ی Invalid Sender
# پیام‌هایی که شناسه‌‌ی فرستنده‌‌‌شان نامعتبر است ولی پیام بدنه معتبری دارند. اگر پیام از این دسته بود عبارت Invalid Sender را چاپ کنید.
#
# دسته‌ی Invalid Content
# پیام‌هایی که بدنه‌‌ی آن‌ها نامعتبر است ولی شناسه فرستنده‌شان معتبر است. اگر پیام از این دسته بود عبارت Invalid Content را چاپ کنید.
#
# دسته‌ی Fully Invalid
# پیام‌هایی که فرستنده و بدنه‌ی نامعتبر داشته باشند. اگر پیام از این دسته بود عبارت Fully Invalid را چاپ کنید.
# تابعی با نام real_numbers بنویسید که لیستی از اعداد (به‌صورت رشته‌ای) را به عنوان ورودی دریافت کند و برای هریک از اعضای این لیست بررسی کند که آیا این عدد، عدد حقیقی صحیح است یا خیر. تابع شما باید لیستی به عنوان جواب برگرداند که اگر عضو iام لیست ورودی داده شده یک عدد حقیقی صحیح است؛ عضو iام لیست جواب دارای مقدار LEGAL در غیر این صورت مقدار ILLEGAL را داشته باشد .
import re


def real_numbers(numbers):
    main_list = []
    for item in numbers:
        if re.match(r'^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$', item):
            main_list.append("LEGAL")
        else:
            main_list.append("ILLEGAL")
    return main_list


real_numbers(['1.5e+2', '3.', '1.1.1', '1+e5'])
