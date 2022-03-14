import re


def words_check(text):
    split_list = text.split()
    assistant_list = []  # for split good word and bad word
    for word in split_list:
        # print(word,len(word),re.findall(r'[\W\d\_]', word),len(re.findall(r'[\W\d\_]', word)))
        if len(re.findall(r'[\W\d\_]', word)) >= len(word) / 2:
            pass
        else:
            assistant_list.append(word)
    # print(assistant_list)

    main_list = []

    # print(assistant_list)

    for word in assistant_list:
        expect_word = word
        for char in word:
            if re.findall(r'[\W\d\?_]', char):
                expect_word = expect_word.replace(char, '')
        main_list.append(expect_word)

    main_list2 = []
    result = ''
    for item in main_list:
        result += item.title() + ' '
        main_list2 = result.strip().split()
    main_list2 = list(sorted(main_list2))

    dic = dict()
    for item in main_list2:
        dic[item] = main_list2.count(item)
    return dic


print(words_check(text='''HeLLLO_O My________________FRIEND
HOW ARE YOUUUUU?___?
I Don'T KNow Y_O_U_R_N_A_M_E yet !!!!!!!!
'''))
