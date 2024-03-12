# Завдання 1
# Створіть клас Student з атрибутами name та age.
# Додайте метод print_info, який виведе інформацію про
# студента у на вигляді "Ім'я: {name}, Вік: {age}".

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Ім'я студента - {self.name} та його вік {self.age}")


student1 = Student("Іван", 20)
student1.print_info()
