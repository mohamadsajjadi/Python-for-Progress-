import csv

participant_and_answer_dict = dict()
data_list = []
main_list = []
data_dict = dict()
result_dict = dict()


def ready_up():
    with open("esm_famil_data.csv", 'r', encoding="utf-8") as csvfile:
        data = csv.DictReader(csvfile)
        for line in data:
            for key in line.keys():
                if line[key]:
                    if key in data_dict.keys():
                        data_dict[key].append(line[key].replace(" ", ""))
                    else:
                        data_dict[key] = [line[key].replace(" ", "")]
        # print(data_dict)


def add_participant(participant, answers):
    participant_and_answer_dict[participant] = answers
    result_dict[participant] = 0


def calculate_all():
    global main_list
    global participant_and_answer_dict
    global data_dict

    # مقدار جواب ها رو میریزم توی یه لیست تا بتونم بهتر باهاش کار کنم برای حساب کتاب امتیازات
    for item in participant_and_answer_dict.values():
        main_list.append(list(item.values()))
    # print(main_list)

    for i in range(6):
        answer_dict = dict()  # ساختمش برای اینکه چک کنم مثلا اسم بردیا توش هست یا نه که بفهمم آیا تکرار شده یا نه
        flag = True
        for j in range(len(main_list)):
            main_list[j][i] = main_list[j][i].replace(" ", "")
            if main_list[j][i] == '':
                flag = False
            if main_list[j][i] in answer_dict.keys():  # چک میکنه بردیا تکرار شده یا نه
                answer_dict[main_list[j][i]] = True
            else:
                answer_dict[main_list[j][i]] = False

        if flag:  # فیلد مربوطه خالی نیست
            for k in range(len(main_list)):
                # بردیا هست ولی تکرار نشده مثلا
                if main_list[k][i] in list(data_dict.values())[i] and not answer_dict[main_list[k][i]]:
                    result_dict[list(participant_and_answer_dict.keys())[k]] += 10
                # بردیا هست ولی تکرار شده
                if main_list[k][i] in list(data_dict.values())[i] and answer_dict[main_list[k][i]]:
                    result_dict[list(participant_and_answer_dict.keys())[k]] += 5
        else:  # فیلد مربوطه خالی هست
            for k in range(len(main_list)):
                # بردیا هست ولی تکرار نشده مثلا
                if main_list[k][i] in list(data_dict.values())[i] and not answer_dict[main_list[k][i]]:
                    result_dict[list(participant_and_answer_dict.keys())[k]] += 15
                if main_list[k][i] in list(data_dict.values())[i] and answer_dict[main_list[k][i]]:
                    result_dict[list(participant_and_answer_dict.keys())[k]] += 10
        # print(answer_dict)
    return result_dict


ready_up()
add_participant(participant='salib',
                answers={'esm': 'علی', 'famil': 'عبدی', 'keshvar': 'عمان', 'rang': 'عسلی',
                         'ashia': 'عینک', 'ghaza': 'عدسی'})
add_participant(participant='mina',
                answers={'esm': 'علی', 'famil': 'عباسی', 'keshvar': 'عراق', 'rang': 'عدسی',
                         'ashia': 'عینک ها', 'ghaza': 'عدس پلو'})
add_participant(participant='saman',
                answers={'esm': 'علی', 'famil': 'عمران', 'keshvar': 'عراق', 'rang': 'عدسی',
                         'ashia': 'عصای', 'ghaza': 'عدس پلو'})
print(calculate_all())
