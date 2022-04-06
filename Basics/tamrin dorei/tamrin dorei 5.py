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
import re


def valid_sender(my_sender):
    return not my_sender.isdigit()


def valid_content(my_content):
    main_length = len(re.findall(r'[\W]', my_content)) - len(re.findall(r' ', my_content))
    if main_length > len(my_content) // 2 and len(re.findall('spam', my_content.lower())) != 0:
        return False
    return True


# def has_spam(my_content):
#     return len(re.findall('spam', my_content.lower())) != 0


input_sender = input()
input_content = input()

if valid_sender(input_sender) and valid_content(input_content):
    print("Not Spam")
elif not valid_sender(input_sender) and valid_content(input_content):
    print("Invalid Sender")
elif valid_sender(input_sender) and not valid_content(input_content):
    print("Invalid Content")
else:
    print("Fully Invalid")
