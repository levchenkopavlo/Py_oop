# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
# дату народження, контактний телефон, місто, країну,
# домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Human:
    def __init__(self, fullName, bDate,tel,city, country):
        self.fullName = fullName
        self.bDate = bDate
        self.tel = tel
        self.city = city
        self.country = country

    def deposit(self, dep):
        self.balance += dep
        return f"Внесену суму додано до балансу. Сумарний баланс: {self.balance}"

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            return f"Ви можете зняти не більше {self.balance}"
        else:
            self.balance -= withdraw
            return f"Вказану суму знято з балансу. Ваш залишок: {self.balance}"


bankAccount1 = BankAccount(234, "client101")
print(bankAccount1.deposit(20))
print(bankAccount1.withdraw(100))
print(bankAccount1.withdraw(200))