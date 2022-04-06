# سلیب که از تنهایی و خانه‌نشینی حوصله‌اش سر رفته تصمیم گرفته که دوستانش را دعوت کند تا با آن‌ها اسم‌فامیل بازی کند.
#
# بعد از رسیدن دوستان سلیب آن‌ها بازی را شروع کردند، اما بعد از تمام شدن دست اول در امتیاز‌دهی دچار مشکل شده‌اند. هیچ‌کس کلمات دیگری را قبول نداشت به همین خاطر نمره‌ی هر کلمه نامشخص بود.
#
# سلیب و دوستانش برنامه‌نویس هستند و فقط به برنامه‌ها اعتماد دارند. به همین خاطر از شما می‌خواهند برایشان برنامه‌ای بنویسید تا با دریافت فایل تمامی کلمات قابل قبول طبق قوانین ذکر شده، بتواند به او و دوستانش نمره‌ای صحیح بدهد.
# سلیب که از تنهایی و خانه‌نشینی حوصله‌اش سر رفته تصمیم گرفته که دوستانش را دعوت کند تا با آن‌ها اسم‌فامیل بازی کند.
#
# بعد از رسیدن دوستان سلیب آن‌ها بازی را شروع کردند، اما بعد از تمام شدن دست اول در امتیاز‌دهی دچار مشکل شده‌اند. هیچ‌کس کلمات دیگری را قبول نداشت به همین خاطر نمره‌ی هر کلمه نامشخص بود.
#
# سلیب و دوستانش برنامه‌نویس هستند و فقط به برنامه‌ها اعتماد دارند. به همین خاطر از شما می‌خواهند برایشان برنامه‌ای بنویسید تا با دریافت فایل تمامی کلمات قابل قبول طبق قوانین ذکر شده، بتواند به او و دوستانش نمره‌ای صحیح بدهد.

# قوانین امتیاز دهی بازی
# ۱- اگر برای این فیلد همه‌ی بازیکنان جوابی را ارائه کرده باشند:
#
# اگر بازیکن پاسخی ارائه کرده باشد که در لیست کلمات قابل قبول نیست، ۰ امتیاز می‌گیرد.
# اگر بازیکن پاسخی تکراری داده باشد ( مثلا برای غذا سه نفر پیتزا نوشته باشند )، ۵ امتیاز می‌گیرد.
# اگر بازیکن پاسخ متمایزی داده باشد ۱۰ امتیاز می‌گیرد.

# ۲- اگر بازیکنی وجود داشته باشد که برای این فیلد پاسخی ارائه نکرده باشد:
# اگر بازیکن پاسخی ارائه کرده باشد که در لیست کلمات قابل قبول نیست و یا پاسخی ارائه نکرده باشد، ۰ امتیاز می‌گیرد.
# اگر بازیکن پاسخی تکراری داده باشد ( مثلا برای غذا سه نفر پیتزا نوشته باشند )، ۱۰ امتیاز می‌گیرد.
# اگر بازیکن پاسخ متمایزی داده باشد ۱۵ امتیاز می‌گیرد.

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
