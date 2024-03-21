# Завдання 1
# До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
# створених об’єктів класу «Людина».
from datetime import datetime


class Contact:
    count = 0

    def __init__(self, fullName="", bDate=None, tel="", city="", country="", street=""):
        Contact.count += 1
        self.fullName = fullName
        self.bDate = bDate
        self.tel = tel
        self.city = city
        self.country = country
        self.street = street

    @staticmethod
    def get_object_count():
        return Contact.count

    @staticmethod
    def get_fullName():
        return se

    def info(self):
        if self.fullName == "":
            return None
        else:
            return f"ПІБ: {self.fullName};\nдата народження: {self.bDate.strftime('%d.%m.%Y')};\nКонтактний телефон: {self.tel};\nМісто: {self.city};\nКраїна: {self.country};\nАдреса: {self.street}"

    def input_data(self):
        self.fullName = input("Введіть ПІБ: ")
        date = input("Введіть дату народження (дд.мм.рррр): ")
        self.bDate = datetime.strptime(date, "%d.%m.%Y")
        self.tel = input("Введіть телефон: ")
        self.city = input("Введіть місто: ")
        self.country = input("Введіть країну: ")
        self.street = input("Введіть вулицю: ")

    def __str__(self):
        return [self.fullName, self.bDate, self.tel, self.city, self.country, self.street]

    def __lt__(self, other):
        return self.bDate > other.bDate

    def __gt__(self, other):
        return self.bDate < other.bDate

    def __le__(self, other):
        return self.bDate >= other.bDate

    def __ge__(self, other):
        return self.bDate <= other.bDate

    def __eq__(self, other):
        return self.fullName == other.fullName and self.bDate == other.bDate

    def __ne__(self, other):
        return self.fullName != other.fullName or self.bDate != other.bDate

    def work(self):
        print(f"Одне слоненя. Двоє слоненят....")

    def sleep(self):
        print(f"Я не хочу спати, у мене безсоння.")

    def eat(self):
        print(f"Cookies!! Om nom nom!")


human1 = Contact("Петрик П'яточкін", datetime(1990, 3, 13, 0, 0), "222-22-22", "Київ", "Україна", "В. Чорновола")
human2 = Contact("Миколка П'яточкін", datetime(1992, 5, 3, 0, 0), "333-33-33", "Київ", "Україна", "В. Чорновола")
human4 = Contact("Петрик П'яточкін", datetime(1990, 3, 13, 0, 0), "222-22-22", "Київ", "Україна", "В. Чорновола")
print(human1.info())

human3 = Contact()
# human3.input_data()
print(human3.__str__())
print(human3.info())

print(human1 > human2)
print(Contact.get_object_count())
print(Contact.count)
