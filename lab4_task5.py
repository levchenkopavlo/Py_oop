# Завдання 5
# Створіть клас Character, який має атрибути name, health
# та damage. Реалізуйте метод класу attack, який виводить
# повідомлення про атаку гравця.

class Character:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    def get_damage(self):
        return self.__damage

    # @staticmethod
    def attack(self, other):
        if other.__damage>self.__health:
            return f'{self.__name} програв'
        else:
            self.__health -= other.__damage
            return f'{self.__name} атакував {other.__name}, залишок healt: {self.__health}'


user1 = Character("user1", 100, 8)
user2 = Character("user2", 120, 7)

print(user2.attack(user1))
