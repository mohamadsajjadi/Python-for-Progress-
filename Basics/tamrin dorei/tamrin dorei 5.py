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


