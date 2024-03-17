# Завдання 2
# До вже реалізованого класу «Місто» додайте конструктор
# та необхідні перевантажені методи.


class City:
    def __init__(self, name="", region="", country="", population=0, zipCode="", telCode=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipCode = zipCode
        self.telCode = telCode

    def __str__(self):
        return [self.name, self.region, self.country, self.population, self.zipCode, self.zipCode]

    def __eq__(self, other):
        return self.name == other.name and self.zipCode == other.zipCode

    def __lt__(self, other):
        return self.population < other.population

    def __gt__(self, other):
        return self.population > other.population

    def __le__(self, other):
        return self.population <= other.population

    def __ge__(self, other):
        return self.population >= other.population

    def __ne__(self, other):
        return self.zipCode != other.zipCode

    def input_data(self):
        while True:
            self.name = input("Введіть назву міста: ")
            self.region = input("Введіть регіон(область): ")
            self.country = input("Введіть країну: ")
            self.population = input("Введіть кількість населення: ")
            self.zipCode = input("Введіть поштовий код: ")
            self.telCode = input("Введіть код телефону міста: ")
            if self.name == "" or self.region == "" or self.country == "" or self.zipCode == "" or not self.telCode.replace(
                    "+", "").isdigit():
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                break

    def info(self):
        return f"Назва: {self.name};\nРегіон: {self.region};\nКраїна: {self.country};\nКількість жителів: {self.population};\nПоштовий код: {self.zipCode};\nТелефонний код: {self.telCode};"

    def populationUp(self, number: int):
        self.population += number

    def populationDown(self, number: int):
        if self.population < number:
            self.population = 0
        else:
            self.population -= number

    def demolish(self):
        print(f"Disaster! {self.name} is destroyed. Save yourself!!")


city1 = City("Toronto", "Ontario", "Canada", 2794000, "416", "+1 905")
print(city1.info())
city1.populationUp(10000000)
print(city1.population)
city1.demolish()
city2 = City()
city2.input_data()
print(city2.info())