# Завдання 3
#  До вже реалізованого класу «Автомобіль» додайте
# необхідні перевантажені методи та оператори.
import datetime


class Car:
    def __init__(self, brand="", model="", year=0, capacity=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.capacity = capacity

    def input_data(self):
        self.brand = input("Введіть назву бренду: ")
        self.model = input("Введіть модель: ")
        self.year = int(input("Введіть рік випуску: "))
        self.capacity = int(input("Введіть місткість: "))

    def __str__(self):
        return [self.brand, self.model, self.year, self.capacity]

    def show(self):
        return f"Brand: {self.brand};\nModel: {self.model};\nYear: {self.year};\nCapacity: {self.capacity}."

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __ne__(self, other):
        return self.brand != other.brand or self.model != other.model

    def start_engine(self):
        print(f"Двигун {self.brand} {self.model} запущено")


car1 = Car("Tesla", "X", 2023, 4)
car2 = Car("Opel", "Astra", 2012, 5)
print(car1.show())
print(car1.__str__())
print(car1 != car2)
car3 = Car()
car3.input_data()
print(car3.show())
