# در این تمرین باید یک نوع داده‌ای (Data Type) جدید بسازید که در پایتون وجود ندارد!
#
# نام این نوع داده‌ای، Strint است و به صورت زیر تعریف می‌شود:
#
# مقایسه اعداد در Strint
# یک Strint به شرطی نسبت به Strint دیگر:
#
# کوچک‌تر است که رقم یکان آن، از رقم یکان دیگری کوچک‌تر باشد. مثلا 84 از 39 کوچک‌تر است؛ چون 4 از 9 کوچک‌تر است.
# بزرگ‌تر است که رقم یکان آن، از رقم یکان دیگری بزرگ‌تر باشد. مثلا 39 از 84 بزرگ‌تر است؛ چون 9 از 4 بزرگ‌تر است.
# مساوی است که رقم یکان آن، با رقم یکان دیگری مساوی باشد. مثلا 84 با 34 مساوی است چون رقم یکان آن‌ها برابر است.
# جمع و تفریق اعداد در Strint
# جمع دو Strint از اضافه شدن Strint دوم به انتهای Strint اول بدست می‌آید. مثلا 84 + 39 برابر 8439 ولی 39 + 84 برابر 3984 است.
# تفاضل دو Strint از حذف شدن Strint دوم از انتهای Strint اول بدست می‌آید. مثلا 8439 - 39 برابر 84 و 8439 - 8439 برابر 0 هستند (توجه کنید که اگر تفاضل دو عدد صحیح نبود، باید استثنایی با پیغام 'The subtraction is not valid!' پرتاب شود.)
# طول و فراخوانی اعداد در Strint
# طول یک Strint از تعداد رقم‌های آن بدست می‌آید. مثلا طول 232425 برابر 6 است.
# با فراخوانی یک Strint، کاراکتر‌های آن به صورت فارسی چاپ می‌شوند. مثلا هنگام فراخوانی این نوع داده‌ای، برای مقدار 232425، مقدار ۲۳۲۴۲۵ بازگردانده می‌شود.

class Strint(int):

    def __lt__(self, other):
        return self % 10 < other % 10

    def __gt__(self, other):
        return self % 10 > other % 10

    def __le__(self, other):
        return self % 10 <= other % 10

    def __ge__(self, other):
        return self % 10 >= other % 10

    def __eq__(self, other):
        return self % 10 == other % 10

    def __ne__(self, other):
        return self % 10 != other % 10

    def __add__(self, other):
        result = str(self) + str(other)
        return int(result)

    def __sub__(self, other):
        s1 = str(self)
        # print(s1)
        s2 = str(other)
        s3 = str(s1[-len(s2):])
        # print(s3)
        if int(s2) == int(s3) and len(s1) == len(s2):
            return int(0)
        elif int(s2) == int(s3):
            return int(s1[:len(s1) - len(s2)])
        else:
            raise Exception('The subtraction is not valid!')

    def __len__(self):
        self = str(self)
        return len(self)

    def __call__(self):
        self = str(self)
        ans = ''
        my_dict = {"0": "۰", "1": "۱", "2": "۲", "3": "۳", "4": "۴", "5": "۵", "6": "۶", "7": "۷", "8": "۸", "9": "۹"}
        for number in self:
            ans += my_dict[number]
        return ans


print(Strint(500) - Strint(0))
