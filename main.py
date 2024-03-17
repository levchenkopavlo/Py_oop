# Завдання 3
# До вже реалізованого класу «Країна» додайте конструктор та необхідні перевантажені методи
class Country:
    def __init__(self, name="", continent="", population=0, capital="", telCode="", cities=None):
        self.name = name
        self.continent = continent
        self.population = population
        self.capital = capital
        self.telCode = telCode
        self.cities = cities

    def __str__(self):
        return [self.name, self.continent, self.population, self.capital, self.telCode, self.cities]

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.population < other.population

    def __gt__(self, other):
        return self.population > other.population

    def __le__(self, other):
        return self.population <= other.population

    def __ge__(self, other):
        return self.population >= other.population

    def __ne__(self, other):
        return self.name != other.name

    def input_data(self):
        while True:
            self.name = input("Введіть назву країни: ")
            self.continent = input("Введіть назву континенту: ")
            self.population = input("Введіть кількість населення: ")
            self.capital = input("Введіть столицю країни: ")
            self.telCode = input("Введіть код телефону країни: ")
            self.cities = input("Введіть основні міста країни (через пробіл): ").split()
            if self.name == "" or self.continent == "" or self.capital == "" or not self.telCode.replace(
                    "+", "").isdigit() or not self.population.isdigit():
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                self.population = int(self.population)
                break

    def info(self):
        return f"Назва: {self.name};\nКонтинент: {self.continent};\nСтолиця: {self.capital};\nКількість жителів: {self.population};\nТелефонний код: {self.telCode};\nМіста: {', '.join(self.cities)}."

    def populationUp(self, number: int):
        self.population += number

    def populationDown(self, number: int):
        if self.population < number:
            self.population = 0
        else:
            self.population -= number

    def diplomatic(self, rel, country):

        return f"Встановлено дипломатичні стосунки: {rel}, з країною {country}."

    def help(self, type, country):

        return f"Надіслано {type} допомогу країні {country}."


country1 = Country("Canada", "North America", 38250000, "Ottawa", "+1",
                   ["Ottawa", "Toronto", "Montreal", "Calgary", "Vancouver", "Winnipeg"])
print(country1.info())
country1.populationUp(1000000)
print(country1.diplomatic("безвіз", "USA"))
country2 = Country()
country2.input_data()
print(country2.info())
print(country2.__str__())
