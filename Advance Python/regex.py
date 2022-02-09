import re


def validate_email(email):
    if re.match(r'^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$', email):
        return True
    else:
        return False


def validate_phone(number):
    if re.match(r'^[[\+989]?[00989]?[09]?][0-9]{9}$', number):
        return True
    else:
        return False


# email = 'sample@school.edu'
# print(validate_email(email))
phone = '09215546321'
print(validate_phone(phone))
