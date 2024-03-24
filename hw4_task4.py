# Завдання 4
#  Створіть клас InformationSystem, який має атрибут data
# - словник, де ключі - це імена користувачів, а значення -
# список їх контактів. Реалізуйте методи класу для додавання
# нових користувачів та їх контактів.

class InformationSystem:
    __data = {}

    @staticmethod
    def set_user(user):
        if user not in InformationSystem.__data:
            InformationSystem.__data[user] = []

    @staticmethod
    def set_contacts(user, *args):
        InformationSystem.__data[user] = list(args)

    @staticmethod
    def add_contacts(user, *args):
        InformationSystem.__data[user].append(*args)

    @staticmethod
    def get_user():
        return list(InformationSystem.__data.keys())

    @staticmethod
    def get_contacts(user):
        return InformationSystem.__data[user]


InformationSystem.set_user("Vano")
print(InformationSystem.get_user())
InformationSystem.set_user("Петрик П'яточкін")
print(InformationSystem.get_user())
InformationSystem.set_contacts('Vano', "222-22-22", "1@1.com")
print(InformationSystem.get_contacts('Vano'))
print(InformationSystem.get_contacts("Петрик П'яточкін"))
InformationSystem.add_contacts("Vano", "333-33-33")
print(InformationSystem.get_contacts('Vano'))
