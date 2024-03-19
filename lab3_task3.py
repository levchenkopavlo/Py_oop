# Завдання 3
# Створіть клас "Електронний Гаманець" додавши
# можливість видаляти та додавати гроші, а також перевіряти
# баланс

class Wallet:
    def __init__(self, summ=0):
        self.__summ = summ

    def set_income(self, income):
        self.__summ += income

    def set_withdraw(self, withdraw):
        if self.__summ <= withdraw:
            print("no money")
        else:
            self.__summ -= withdraw

    def get_ballance(self):
        return self.__summ


wallet1 = Wallet()
print(wallet1.get_ballance())
wallet1.set_income(1000)
wallet1.set_income(10)
print(wallet1.get_ballance())
wallet1.set_withdraw(600)
print(wallet1.get_ballance())
wallet1.set_withdraw(700)
print(wallet1.get_ballance())
