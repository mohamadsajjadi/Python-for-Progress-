def decorator(validator):
    def higher_function(func):
        def inner_function(*args):
            if validator(*args):
                result = func(*args)
                return result
            else:
                return "error"

        return inner_function

    return higher_function


