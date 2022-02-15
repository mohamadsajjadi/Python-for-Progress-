def check_registration_rules(**kwargs):
    for keys in kwargs.keys():
        # print(type(keys))
        if keys == 'quera':
            del kwargs[keys]
    print(list(kwargs.keys()))

    # if len(keys) < 4 or keys == 'quera' or keys == 'codecup' or len(values) < 6 or str(values).isnumeric():
    # del kwargs[keys]
    #     if len(keys) < 4:
    #         del kwargs[keys]
    #     elif keys == 'quera' or keys == 'codecup':
    #         del kwargs[keys]
    #     elif len(values) < 6:
    #         del kwargs[keys]
    #     elif str(values).isnumeric():
    #         del kwargs[keys]
    # print(list(kwargs.keys()))


check_registration_rules(quera='qwerty80', mmdreza='monday80', ali="aliali@", mammad="salam")
# data = {'username': 'ali', 'password': '2420879422'}
# del data['username']
# print(data)
