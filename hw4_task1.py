# Завдання 1
# До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
# класу «Дріб».
class Fraction:
    __counter = 0

    @staticmethod
    def get_counter():
        return Fraction.__counter

    def __init__(self, numerator, denominator):
        Fraction.__counter += 1
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.__numerator * other.__denominator
        new_denominator = self.__denominator * other.__numerator
        return Fraction(new_numerator, new_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
print(fraction1 + fraction2)
print(Fraction.get_counter())