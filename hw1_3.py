# Завдання 3
# Створіть клас «Країна». Збережіть у класі: назву країни,
# назву континенту, кількість жителів країни, телефонний
# код країни, назву столиці, назву міст країни. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій.
class Country:
    def __init__(self, name, continent, population: int, capital, telCode, cities: list):
        self.name = name
        self.continent = continent
        self.population = population
        self.capital = capital
        self.telCode = telCode
        self.cities = cities

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