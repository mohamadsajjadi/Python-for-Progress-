# تابعی با نام real_numbers بنویسید که لیستی از اعداد (به‌صورت رشته‌ای) را به عنوان ورودی دریافت کند و برای هریک از اعضای این لیست بررسی کند که آیا این عدد، عدد حقیقی صحیح است یا خیر. تابع شما باید لیستی به عنوان جواب برگرداند که اگر عضو iام لیست ورودی داده شده یک عدد حقیقی صحیح است؛ عضو iام لیست جواب دارای مقدار LEGAL در غیر این صورت مقدار ILLEGAL را داشته باشد .
# test case
# words_check("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a""")
# {'A': 2, 'For': 1, 'Friends': 1, 'Hello': 1, 'Is': 1, 'My': 1, 'Test': 1, 'This': 1, 'Your': 1}
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
