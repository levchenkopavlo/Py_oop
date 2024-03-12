import math
# Завдання 2
#  Створіть клас Circle з атрибутом radius та методом
# area, який поверне площу кола з вказаним радіусом.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # print(f"{self.radius ** 2 * 3.14}")
        return self.radius ** 2 * math.pi


circle1 = Circle(5)
print(f"{circle1.area()}")
