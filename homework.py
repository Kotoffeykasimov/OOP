

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
       return (f'имя : {self.name} \nфамилия : {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
               f'\nЗавершенные курсы:{", ".join(self.finished_courses) if len(self.finished_courses) > 0 else " нет завершенных курсов"}')


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lecturer_grades(self,lecturer, course, grade):

        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else :
                lecturer.grades[course] = [grade]

        else: return 'ошибка'

    def average_grade(self):        #расчет средней оценки за ДЗ у студентов
        self.new_dict = {}
        full_len=0
        for i, j in self.grades.items():
            self.new_dict[i] = sum(j)
            full_len += len(j)
        res = sum(self.new_dict.values())/full_len
        return res

    def rate(self,student1):            # Сравнение средней оценки у двух студентов
        if self.average_grade() == student1.average_grade():
            print(f'оценки {self.name}  {self.surname} и {student1.name} {student1.surname} равны')
        else:
            res = f'больше'if self.average_grade() > student1.average_grade() else f'меньше'
            a =(f'средняя оценка за домашнюю работу {self.name}  {self.surname} {res} чем у {student1.name} {student1.surname}')
            return a


def aver_for_course(student_list, course):      #cредняя оценка студентов за ДЗ в рамках курса
    a = 0
    len_all = 0
    for student in student_list:

        if course  in student.grades :
            a += sum(student.grades[course])
            len_all += len(student.grades[course])
    result = (a/len_all)

    return result



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def __str__(self):
        return f'имя : {self.name} \nфамилия : {self.surname}'

    def rate_hw(self, student, course, grade):      # выставление оценок ментором - студенту
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def average_grade(self):  # расчет средней оценки за ДЗ у студентов
        self.new_dict = {}
        full_len = 0
        for i, j in self.grades.items():
            self.new_dict[i] = sum(j)
            full_len += len(j)
        res = sum(self.new_dict.values()) / full_len
        return res

    def __str__(self):
       return f'имя: {self.name} \nфамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()} '

    def rate(self,lecturer2):       #сравнение средней оценки за лекции двух лекторов
        if self.average_grade() == lecturer2.average_grade():
            print(f'оценки {self.name}  {self.surname} и {lecturer2.name} {lecturer2.surname} равны')
        else:
            a = f'больше'if self.average_grade() > lecturer2.average_grade() else f'меньше'
            res=f'средняя оценка за лекции {self.name}  {self.surname} {a} чем у {lecturer2.name} {lecturer2.surname}'
            return res

def aver_for_course_1(lecturer_list, course):  # cредняя оценка лекторов за лекции в рамках курса
    a = 0
    len_all = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            a += sum(lecturer.grades[course])
            len_all += len(lecturer.grades[course])
    result = (a / len_all)

    return result




best_student = Student('Дядя', 'Фёдор', 'your_gender')
bad_student = Student('Сергей', 'Петров', 'мужик')
best_student.courses_in_progress += ['Python','java','Data Science']
best_student.finished_courses += ['PHP']
bad_student.courses_in_progress += ['Data Science','Python','java',]


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python','Data Science']

cool_mentor.rate_hw(bad_student, 'Python', 10)
cool_mentor.rate_hw(bad_student, 'Python', 5)
cool_mentor.rate_hw(bad_student, 'Data Science', 7)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)


good_lecturer = Lecturer('Ruoy', 'Eman')

good_lecturer1 = Lecturer('Костян' ,'Моисеев')


good_lecturer.courses_attached += ['Python','Data Science']
good_lecturer1.courses_attached += ['java','Data Science','Python']

bad_student.lecturer_grades(good_lecturer, 'Python', 5)
bad_student.lecturer_grades(good_lecturer1, 'Data Science', 10)
bad_student.lecturer_grades(good_lecturer1, 'Python', 10)


reviewer = Reviewer('Зилли', 'Боба')

reviewer1 = Reviewer('Джон', 'Кофи')


print(reviewer)   # инфо о ревьювере
print(good_lecturer)    # инфо о лекторе
print(best_student)     # инфо о студенте
print( best_student.rate(bad_student))  # сравнение средней оценки двух студентов
print(good_lecturer1.rate(good_lecturer))  # сравнение средней оценки двух лекторов
print(good_lecturer.grades) # Оценки лектора от студентов за лекции
print(best_student.average_grade())#средняя оценка студента
print(good_lecturer1.average_grade())#средняя оценка лектора
print(best_student.grades)  #  оценки студента
print(best_student.grades.get('Python','нет оценок за данный курс'))    # оценки студента за курс
print(aver_for_course([bad_student, best_student],'Python'))    # cредняя оценка списка студентов за ДЗ в рамках курса
print(aver_for_course_1([good_lecturer, good_lecturer1 ],'Python')) #cредняя оценка списка лекторов за лекции в рамках курса
