# Завдання 6
# Створіть клас Student, який має атрибути name, age,
# grade та courses. Реалізуйте метод класу add_course, який
# додає новий предмет до списку курсів студента
class Student:
    def __init__(self, name, age, grade, courses=[]):
        self.__name = name
        self.__age = age
        self.__grade = grade
        self.__courses = courses

    def add_course(self, course):
        self.__courses.append(course)

    def get_courses(self):
        return self.__courses


student1 = Student("student", 23, 6)
student1.add_course("ООП")
print(student1.get_courses())
student1.add_course("Фізика")
print(student1.get_courses())
