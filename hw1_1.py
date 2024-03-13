# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Human:
    def __init__(self, fullName, bDate, tel, city, country, street):
        self.fullName = fullName
        self.bDate = bDate
        self.tel = tel
        self.city = city
        self.country = country
        self.street = street

    def info(self):
        return f"Ім'я: {self.fullName};\nдата народження: {self.bDate};\nКонтактний телефон: {self.tel};\nМісто: {self.city};\nКраїна: {self.country};\nАдреса: {self.street}"

    def work(self):
        print(f"Одне слоненя. Двоє слоненят....")

    def sleep(self):
        print(f"Я не хочу спати, у мене безсоння.")

    def eat(self):
        print(f"Cookies!! Om nom nom!")


human1 = Human("Петрик П'яточкін", "13/03/1984", "222-22-22", "Київ", "Україна", "В. Чорновола")
print(human1.info())
human1.work()
human1.eat()
human1.sleep()
