# Завдання 4
#  Створіть клас Car з атрибутами brand (марка
# автомобіля), model (модель) та year (рік випуску).
# Додайте метод start_engine, який виведе повідомлення
# про те, що двигун запущено.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Двигун запущено")


car1 = Car("Tesla","X", "2023")
car1.start_engine()
