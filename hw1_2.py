# Завдання 2
# Створіть клас «Місто». Збережіть у класі: назву міста,
# назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста, телефонний код міста. Реалізуйте
# методи класу для введення-виведення даних та інших операцій.
class City:
    def __init__(self, name, region, country, population: int, zipCode, telCode):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipCode = zipCode
        self.telCode = telCode

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