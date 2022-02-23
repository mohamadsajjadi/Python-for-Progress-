class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    lst = list()
    for item in func_ls:
        try:
            item()
            e = ExceptionProxy(msg='ok!', function=item)
            lst.append(e)
        except Exception as ex:
            e = ExceptionProxy(msg=str(ex), function=item)
            lst.append(e)
    return lst


def f():
    print(1 / 0)


def g():
    pass


tr_ls = transform_exceptions([f, g])

for exception in tr_ls:
    print("msg: " + exception.msg + "\nfunction name: " + exception.function.__name__)
