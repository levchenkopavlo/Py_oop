from datetime import datetime


# Завдання 2
#  Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.
class Stadium:
    def __init__(self, name="", date=None, country="", city="", capacity=0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        date1 = input("Введіть дату відкриття (дд.мм.рррр): ")
        self.date = datetime.strptime(date1, "%d.%m.%Y")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

    def __str__(self):
        return [self.name, self.date, self.country, self.city, self.capacity]

    def show(self):
        return f"Назва: {self.name};\nДата відкриття: {self.date.strftime('%d.%m.%Y')};\nКраїна: {self.country};\nМісто: {self.city};\nCapacity: {self.capacity}."

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date and self.country == other.country and self.city == other.city

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __ne__(self, other):
        return self.name != other.name or self.city != other.city


stadium1 = Stadium("Арена Львів", datetime(2011, 10, 29, 0, 0), "Україна", "Львів", 34900)
stadium2 = Stadium("Чорноморець", datetime(2011, 11, 19, 0, 0), "Україна", "Одеса", 34164)
stadium3 = Stadium()
stadium3.input_data()
print(stadium3.show())
print(stadium3.__str__())
print(stadium1.__str__())
print(stadium1 == stadium2)
print(stadium1 > stadium2)
print(stadium1 < stadium2)
print(stadium1.date.strftime('%d.%m.%Y'))
