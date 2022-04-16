import hashlib
import re


class Site:
    def __init__(self, url_address):
        self.url = url_address
        self.register_users = []
        self.active_users = []

    def show_users(self):
        pass

    def register(self, user):
        if user in self.register_users:
            raise Exception("user already registered")
        else:
            self.register_users.append(user)
            return "register successful"

    def login(self, **kwargs):
        hash_password = hashlib.sha256(kwargs["password"].encode('utf-8')).hexdigest()
        if len(kwargs) == 3:
            for user in self.register_users:
                if kwargs["email"] == user.email and hash_password == user.password and kwargs["username"] == user.username:
                    if user in self.active_users:
                        return "user already logged in"
                    else:
                        self.active_users.append(user)
                        return "login successful"
        elif len(kwargs) == 2 and 'username' in kwargs.keys():
            for user in self.register_users:
                if hash_password == user.password and kwargs["username"] == user.username:
                    if user in self.active_users:
                        return "user already logged in"
                    else:
                        self.active_users.append(user)
                        return "login successful"
        elif len(kwargs) == 2 and 'email' in kwargs.keys():
            for user in self.register_users:
                if hash_password == user.password and kwargs["email"] == user.email:
                    if user in self.active_users:
                        return "user already logged in"
                    else:
                        self.active_users.append(user)
                        return "login successful"
        return "invalid login"

    def logout(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            return "logout successful"
        else:
            return "user is not logged in"

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


class Account:
    def __init__(self, username, password, user_id, phone, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.user_id = self.id_validation(user_id)
        self.phone = self.phone_validation(phone)
        self.email = self.email_validation(email)

    def set_new_password(self, password):
        self.password = self.password_validation(password)

    def username_validation(self, username):
        if re.match(r"^[a-zA-Z]+_[a-zA-Z]+$", username):
            return username
        else:
            raise Exception("invalid username")

    def password_validation(self, password):
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$", password):
            hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return hash_password
        else:
            raise Exception("invalid password")

    def id_validation(self, id):
        if re.match(r"[0-9]{10}", id):
            my_id = str(id)
            control_number = my_id[-1]
            temp_list = my_id[:-1]
            reverse_list = temp_list[::-1]
            sum = 0
            for i in range(len(reverse_list)):
                sum += int(reverse_list[i]) * (i + 2)
            if 2 > sum % 11 == int(control_number):
                return id
            elif sum % 11 >= 2:
                result = 11 - (sum % 11)
                if result == int(control_number):
                    return id
                else:
                    raise Exception("invalid code melli")

            else:
                raise Exception("invalid code melli")
        else:
            raise Exception("invalid code melli")

    def phone_validation(self, phone):
        if re.match(r"^((\+98)|(0))9[0-9]{9}$", phone):
            if phone[0] == '+':
                return '0' + phone[3:]
            else:
                return phone
        else:
            raise Exception("invalid phone number")

    def email_validation(self, email):
        if re.match(r"^[\w\d\_\-\.]+\@[\w\d\_\-\.]+\.[a-zA-Z]{2,5}$", email):
            return email
        else:
            raise Exception("invalid email")

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(func):
    def inner_func(user):
        text = user.replace("_", " ")
        f = func(text)
        new_user = text.title()
        if len(new_user) > 15:
            return f[:20] + new_user[:15] + "..."
        else:
            return f[:20] + new_user

    return inner_func


def verify_change_password(func):
    def inner_func(user, old_pass, new_pass):
        f = func(user, old_pass, new_pass)
        if user.password == hashlib.sha256(old_pass.encode("utf-8")).hexdigest():
            user.set_new_password(new_pass)
        return f

    return inner_func


@show_welcome
def welcome(user):
    return "welcome to our site %s" % user


@verify_change_password
def change_password(user, old_pass, new_pass):
    return "your password is changed successfully."
