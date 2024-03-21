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
        if self.__damage > other.__health:
            return f'{other.__name} програв'
        else:
            other.__health -= self.__damage
            return f'{self.__name} атакував гравця {other.__name}, залишок healt: {other.__health}'


user1 = Character("user1", 100, 8)
user2 = Character("user2", 120, 7)

print(user1.attack(user2))
