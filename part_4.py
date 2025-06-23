class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sums = []

    def __gt__(self, other):
        return self.avarage_rate() > other.avarage_rate()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and
            course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def avarage_rate(self):
        sum_ = 0
        for k, v in self.grades.items():
            for e in v:
                self.sums.append(e)
                sum_ += e
        return sum_ / len(self.sums)

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avarage_rate()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")


class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.sums = []

    def __gt__(self, other):
        return self.avarage_rate() > other.avarage_rate()

    def avarage_rate(self):
        sum_ = 0
        for k, v in self.grades.items():
            for e in v:
                self.sums.append(e)
                sum_ += e
        return sum_ / len(self.sums)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avarage_rate()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

student_list = []
def avarage_hw(student_list, course):
    sum_ = 0
    sums_list = []
    for st in student_list:
        if st in student_list and course in student.grades:
            for k, v in student.grades.items():
                for e in v:
                    sums_list.append(e)
                    sum_ += e
    return f"Средняя оценка за дз: {sum_ / len(sums_list)}"


lecturer_list = []
def avarage_rate(lecturer_list, course):
    sum_ = 0
    sums_list = []
    for lc in lecturer_list:
        if lc in lecturer_list and course in lecturer.grades:
            for k, v in lecturer.grades.items():
                for e in v:
                    sums_list.append(e)
                    sum_ += e
    return f"Средняя оценка за лекции: {sum_ / len(sums_list)}"


student = Student('Иван', 'Иванов', 'М')
student2 = Student('Пётр', 'Петров','М' )

student_list.append(student)
student_list.append(student2)

lecturer = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Once', 'ToldMe')

lecturer_list.append(lecturer)
lecturer_list.append(lecturer2)

reviewer = Reviewer('TheWorld', 'IsGonnaRollMe')
reviewer2 = Reviewer('Shrek', 'ForEver')

student.add_courses('Python')
student2.add_courses('Python')

student.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python', 'Git']

lecturer.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'C++']

reviewer.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'C++']

student.rate_lecture(lecturer, 'Python', 10)
student2.rate_lecture(lecturer, 'Python', 9)

reviewer.rate_hw(student, 'Python', 9.5) ###
reviewer2.rate_hw(student, 'Python', 10)

print(student.avarage_rate())
print(lecturer.avarage_rate())
print(student > lecturer)
print(avarage_hw(student_list, 'Python'))
print(avarage_rate(lecturer_list, 'Python'))
