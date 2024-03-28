# Завдання 4
# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця.
# Для базового класу це може бути рядок із написом «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.
class Employer:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def print(self):
        print(f'This is Employer class')

    def __str__(self):
        return f'{self.__dict__}'


class President(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print(f'This is President')


class Manager(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print(f'This is {self.__class__.__name__}')


class Worker(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)


president1 = President('John',65)
president1.print()
print(president1)
manager1 = Manager('Jill',33)
manager1.print()
print(manager1)
worker1 = Worker('Joe',40)
worker1.print()
print(worker1)
