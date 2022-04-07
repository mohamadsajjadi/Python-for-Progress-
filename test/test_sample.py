def outer_func(fname, lname):
    def main_func(func):
        def inner_func():
            if fname == firstname and lname == lastname:
                f = func()
                return f
            else:
                print("fuck")

        return inner_func

    return main_func


firstname = input("Enter your firstname:\n")
lastname = input("Enter your lastname:\n")


@outer_func(firstname, lastname)
def login():
    print("you are my friend!")


login()
