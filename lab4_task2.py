import math


# Завдання 2
# Створіть клас для підрахунку площі геометричних
# фігур. Клас має надавати функціональність підрахунку
# площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
# підрахунку площі реалізуйте за допомогою статичних
# методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом

class Area:
    counter = 0

    @staticmethod
    def area_square(len_a):
        Area.counter += 1
        return len_a * len_a

    @staticmethod
    def area_rectangle(len_a, len_b):
        Area.counter += 1
        return len_a * len_b

    @staticmethod
    def area_triangle(len_a, len_b, len_c):
        Area.counter += 1
        p = (len_a + len_b + len_c) / 2
        return math.sqrt(p * (p - len_a) * (p - len_b) * (p - len_c))

    @staticmethod
    def area_triangle_2(base, height):
        Area.counter += 1
        return 0.5 * base * height

    @staticmethod
    def area_diamond(diag_1, diag_2):
        Area.counter += 1
        return 0.5 * diag_1 * diag_2


print(Area.area_square(4))
print(Area.area_rectangle(4, 6))
print(Area.area_triangle(3, 4, 5, ))
print(Area.area_triangle_2(3, 4))

print(f'{Area.counter=}')
