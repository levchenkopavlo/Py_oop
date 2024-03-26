# Створіть клас Passport (паспорт), який міститиме
# паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте
# клас ForeignPassport (закордонний паспорт), похідний від Passport.
# Нагадаємо, що закордонний паспорт містить, крім
# паспортних даних, дані про візи і номер закордонного паспорта.
# Кожен із класів має містити необхідні методи.

class Passport:
    def __init__(self, country, name, passport_id):
        self._country = country
        self._name = name
        self._passport_id = passport_id

    def get_info(self):
        print(
            f"Name: {self._name};\nCountry: {self._country};\nPassport:{self._passport_id}.")


class ForeignPassport(Passport):
    def __init__(self, country, name, passport_id, visas, foreign_passport_id):
        super().__init__(country, name, passport_id)
        self._visas = visas
        self._foreign_passport_id = foreign_passport_id

    def get_info(self):
        print(
            f"Name: {self._name};\nCountry: {self._country};\nPassport:{self._passport_id}.")


# Приклад використання
passport = Passport("Ukraine", "John", "aq123456")
passport.get_info()

print()

foreign_passport = ForeignPassport("Ukraine", "John", "123456", "Canada visa", "qwe12435")
foreign_passport.get_info()
