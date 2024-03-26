# Завдання 3
# Створіть базовий клас «Тварина» та похідні класи:
# «Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
# конструктора ім’я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.

class Animal:
    def __init__(self, name, family, sound):
        self._name = name
        self._family = family
        self._sound = sound

    def get_info(self):
        print(
            f"Назва: {self._name};\nСімейство: {self._family};\nЗвуки:{self._sound}.")


class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Савець", "грррр")


class Crocodile(Animal):
    def __init__(self, name, tail_length):
        super().__init__(name, "Крокодилові", "гр-гр")
        self._tail_length = tail_length


class Kangaroo(Animal):
    def __init__(self, name):
        super().__init__(name, "Сумчастий", "?")


crocodile1 = Crocodile("Крокодил нільський", 1)
crocodile1.get_info()
