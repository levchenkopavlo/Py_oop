# Завдання 2
# Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
# «Колеса», «Двигун», «Двері» та ін.
class Wheel:
    def __init__(self, radius):
        print('init from Wheel')
        self._radius = radius


class Engine:
    def __init__(self, power):
        print('init from Engine')
        self._power = power


class Doors:
    def __init__(self, number):
        print('init from Doors')
        self._number = number


class Auto(Wheel, Engine, Doors):
    def __init__(self, radius, power, door_number):
        super().__init__(radius)
        Engine.__init__(self, power)
        Doors.__init__(self, door_number)

    def info(self):
        print(f'{list(self.__dict__.values())}')


car1 = Auto(18, 144, 2)
car1.info()
