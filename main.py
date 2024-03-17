# Завдання 4
# Реалізуйте клас «Годинник». Збережіть у класі:
# назву моделі годинника, виробника годинника, рік
# випуску, ціну годинника, тип годинника (наручний,
# настінний і т. д.). Реалізуйте конструктор та методи
# класу для введення-виведення даних, а також для
# інших операцій. Використовуйте механізм перевантаження методів.

class Clock:
    def __init__(self, brand="", model="", year=0, clockType="", value=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.clockType = clockType
        self.value = value

    def input_data(self):
        while True:
            self.brand = input("Введіть назву бренду: ")
            self.model = input("Введіть модель: ")
            year = input("Введіть рік випуску: ")
            self.clockType = input("Введіть тип: ")
            value = input("Введіть ціну: ")
            if self.brand == "" or self.model == "" or not year.isdigit() or not value.isdigit():
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                self.year = int(year)
                self.value = int(value)
                break

    def __str__(self):
        return [self.brand, self.model, self.year, self.clockType, self.value]

    def show(self):
        return f"Brand: {self.brand};\nModel: {self.model};\nYear: {self.year};\nType: {self.clockType};\nValue: {self.value}."

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __ne__(self, other):
        return self.brand != other.brand or self.model != other.model
