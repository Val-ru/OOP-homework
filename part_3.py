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


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

student = Student('Some', 'Buddy', 'М')
# best_student = Student('Once', 'ToldMe', 'М')
# best_lecturer = Lecturer('TheWorld', 'IsGonnaRollMe')

student.courses_in_progress += ['Python', 'Git']

lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
student.finished_courses += ['Введение в программирование']

student.rate_lecture(lecturer, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9.9)

print(reviewer)
print(lecturer)
print(student)
print(student > lecturer)