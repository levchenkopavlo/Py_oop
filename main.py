# Завдання 5
# Створіть клас BankAccount з атрибутами balance
# та owner, а також методами deposit та withdraw для
# здійснення операцій з балансом. Реалізуйте перевірку
# на те, що баланс не може стати від'ємним.

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

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
