class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = None
        self.my_dict = dict()

    def __getattr__(self, item):
        if item in dir(self._obj):
            if item in self.my_dict.keys():
                self.my_dict[item] += 1
            else:
                self.my_dict[item] = 1
            self.last_invoked = item
            return getattr(self._obj, item)
        else:
            raise Exception("No Such Method")

    def last_invoked_method(self):
        if self.last_invoked is not None:
            return self.last_invoked
        else:
            raise Exception("No Method Is Invoked")

    def count_of_calls(self, method_name):
        if method_name in self.my_dict.keys():
            return self.my_dict[method_name]
        else:
            return 0

    def was_called(self, method_name):
        if Proxy.count_of_calls(self, method_name) >= 1:
            return True
        else:
            return False


class Radio:
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on


radio = Radio()
radio_proxy = Proxy(radio)
radio_proxy.set_channel(95)
radio_proxy.set_channel(95)
print(radio_proxy)
