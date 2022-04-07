import requests


def process(url):
    try:
        response = requests.get(url).json()
        lst = list()
        for item in response:
            # lst = (lst.append(item['category'])) if item['category'] != '' else None
            if item['category'] != '':
                lst.append(item["category"])
        if len(lst) != 0:
            flag = lst.count(lst[0]) == len(lst)
            if flag:
                return lst[0]
            elif len(lst) == 0 or flag == False:
                return "I can't recognize it"
        else:
            return "I can't recognize it"
    except:
        return 'Bad Query'


print(process(''))
