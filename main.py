# Завдання 2
#  Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.
class Stadium:
    def __init__(self, name, date, country, capacity):
        self.name = name
        self.date = date
        self.country = country
        self.capacity = capacity

    def __add__(self, other):
        self.capacity += other
        return self.capacity
    def __str__(self):


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


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
print(fraction1 + fraction2)
