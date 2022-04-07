# در این تمرین باید یک کلاس به نام Reverse تعریف کنید و در سازنده آن یک لیست را به عنوان ورودی بگیرید. کلاس Reverse باید پیمایش‌شونده باشد و اگر پیموده شود برعکس ترتیب خود لیست اعضای آن خروجی داده شود. دقت کنید که نباید ترتیب اعضای خود لیست عوض شود.
class Reverse:
    def __init__(self, ls):
        self.data = list(ls)
        self.current = len(ls) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        current = self.current
        self.current -= 1
        return self.data.pop(current)


ls = [1, 2, 3, 4, 5]
for it in Reverse(ls):
    print(it)
