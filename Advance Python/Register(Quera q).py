def check_registration_rules(**kwargs):
    lst = list()
    for keys, values in kwargs.items():
        if keys != 'quera' and keys != 'codecup' and len(keys) >= 4 and len(values) >= 6 and not str(values).isnumeric():
            lst.append(keys)
    print(lst)


check_registration_rules(quera='qwerty80', mmdreza='monday80', ali="aliali@", mammad="salam")
