# Завдання 1
# Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
# "email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
# дані можна отримати лише через методи класу.

class User:
    def __init__(self, name="", age="", mail=""):
        self.__name = name
        self.__age = age
        self.__mail = mail


    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, age):
        self.__age = age

    def set_mail(self, mail):
        self.__mail = mail

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_mail(self):
        return self.__mail


user1 = User()
user1.set_name("u1", )
user1.set_mail("u1@mail.com")
print(user1.get_name())
print(user1.get_mail())
