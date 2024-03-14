# Завдання 1
#  Створіть клас «Дріб». Збережіть у класі чисельник
# та знаменник. Реалізуйте методи класу для введеннявиведення даних. Також створіть методи класу для
# виконання арифметичних операцій (додавання, віднімання, множення, ділення і т. д.). До вже
# реалізованого класу «Дріб» додайте необхідні перевантажені методи та оператори.
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
print(fraction1 + fraction2)
