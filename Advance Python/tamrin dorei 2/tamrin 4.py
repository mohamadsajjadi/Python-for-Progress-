import re


# abaac
class Security:

    def encrypt(self, s):
        result = ""
        for i in range(len(s)):
            ascii_code = ord(s[i]) - 96
            count = 0
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    count += 1
                else:
                    break
            result += str(ascii_code * count)
        return result

    def is_social_account_info(self, param):
        if re.match(r"^[A-Z][a-z]+:www\.[a-z0-9\.]+\/[a-z0-9\_]+", param):
            return True
        return False

    def secure(self, info):
        result = []
        s = ' '
        info = info.split()
        for item in info:
            new_string = item
            if self.is_social_account_info(item):
                account = item.split("/")[1]
                encrypt_account = self.encrypt(account)
                new_string = item.replace(item.split("/")[1], encrypt_account)
            result.append(new_string)
        return s.join(result)


s = Security()
print(s.secure(
    "Tell me something boy? Are You Happy in this modern world? Imdb:www.imdb.com/account Or do you need more?"))
