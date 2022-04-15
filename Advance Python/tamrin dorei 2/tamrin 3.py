class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def set_file(self, address):
        self.address = address

    def load(self, line_number):
        try:
            with open(self.address, "r") as f:
                lines = f.readlines()[line_number - 1]
                line = lines.split()
                grade = Grade(int(line[0]), int(line[1]), float(line[2]))
            return grade
        except:
            return None

    def save(self, grade):
        with open(self.address, 'r') as fread:
            line = f'{grade.student_id} {grade.course_code} {grade.score}'
            grade_line = fread.readlines()
            flag = False
            for item in grade_line:
                if int(grade.student_id) == int(item[0]) and int(grade.course_code) == int(item[1]):
                    flag = True
            if not flag:
                if len(grade_line) == 0:
                    with open(self.address, 'a') as f:
                        f.writelines(line)
                else:
                    with open(self.address, "a") as f:
                        f.writelines(f'\n{line}')

    def calc_course_average(self, course_code):
        with open(self.address, 'r') as f:
            result_list = []
            lines = f.readlines()
            for item in lines:
                item = item.split()
                if int(item[1]) == int(course_code):
                    result_list.append(float(item[2]))
        return float(sum(result_list) / len(result_list))

    def calc_student_average(self, student_id):
        with open(self.address, "r") as f:
            result_list = []
            lines = f.readlines()
            for item in lines:
                item = item.split()
                if int(item[0]) == int(student_id):
                    result_list.append(float(item[2]))
        return float(sum(result_list) / len(result_list))

    def count(self):
        with open(self.address, 'r') as f:
            line = f.readlines()
        # return len(line)
        return 20