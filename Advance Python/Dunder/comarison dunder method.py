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
