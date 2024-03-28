# Завдання 3
# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
# методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.

class Pet:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print(f'My name is {self._name}')

    def sound(self):
        print(f'animal sound')

    def info(self):
        print(f'{self.__dict__.values()}')


class Dog(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def sound(self):
        print(f'woof woof')


class Cat(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def sound(self):
        print(f'meu')


class Parrot(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def sound(self):
        print(f'chok chok')


class Hamster(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def sound(self):
        print(f'pi')


dog1 = Dog('Rex', 'labrador')
cat1 = Cat('murko', 'sfinks')
parrot1 = Parrot('Ricci', 'budgie')
dog1.get_name()
dog1.info()
parrot1.get_name()
parrot1.info()
