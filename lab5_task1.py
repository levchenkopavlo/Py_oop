# Завдання 1
# Створіть клас Human, який міститиме інформацію про людину.
# За допомогою механізму успадкування реалізуйте
# клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot
# (містить інформацію про льотчика).
# Кожен із класів має містити необхідні для роботи методи.
class Human:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def set_name(self, new_name):
        self._name = new_name

    def get_info(self):
        print(f"Name: {self._name};\nAge: {self._age};\nGender: {self._gender}.")


class Builder(Human):
    def __init__(self, name, age, gender, specialisation):
        super().__init__(name, age, gender)
        self._spec = specialisation

    def set_spec(self, new_specialisation):
        self._spec = new_specialisation

    def get_info(self):
        print(f"Name: {self._name};\nAge: {self._age};\nGender: {self._gender};\nSpecialist in: {self._spec}.")


class Sailor(Human):
    def __init__(self, name, age, gender, rank):
        super().__init__(name, age, gender)
        self._rank = rank

    def set_rank(self, new_rank):
        self._rank = new_rank

    def get_info(self):
        print(f"Name: {self._name};\nAge: {self._age};\nGender: {self._gender};\nRank: {self._rank}.")

class Pilot(Human):
    def __init__(self, name, age, gender, vehicle_type):
        super().__init__(name, age, gender)
        self._vehicle_type = vehicle_type

    def set_rank(self, new_vehicle_type):
        self._vehicle_type = new_vehicle_type


person1 = Sailor('John', 27, 'male', 'captain')
person1.get_info()
person2 = Builder('Ostin', 32, 'male', 'architect')
person2.get_info()

print()
print(person1.__dict__)
print(person1.__dict__.values())
