# Завдання 3
#  До вже реалізованого класу «Автомобіль» додайте
# необхідні перевантажені методи та оператори.

class Car:
    def __init__(self, brand, model, year, capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.capacity = capacity

    def __str__(self):
        return f"Brand: {self.brand};\nModel: {self.model};\nYear: {self.year};\nCapacity: {self.capacity}."

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __abs__(self):
        return f"ABS function is unlocked"

    def start_engine(self):
        print(f"Двигун {self.brand} {self.model} запущено")


car1 = Car("Tesla", "X", "2023", 4)
car2 = Car("Opel", "Astra", "2012", 5)
car1.start_engine()
