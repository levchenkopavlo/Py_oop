# Завдання 2
# Реалізуйте клас "Кошик для покупок" з можливістю
# додавання товарів та підрахунку загальної вартості.
# Застосуйте інкапсуляцію для забезпечення правильності
# обробки даних.

class Cart:
    def __init__(self, goods=[], value=0):
        self.__goods = goods
        self.__value = value

    def add_goods(self, new_goods, value):
        if new_goods not in self.__goods:
            self.__goods.append(new_goods)
        self.__value += value

    def remove_goods(self, new_goods, value):
        if new_goods in self.__goods:
            self.__goods.remove(new_goods)
            self.__value -= value

    def get_goods(self):
        return self.__goods

    def get_summ(self):
        return self.__value


cart1 = Cart()
cart1.add_goods("banana", 20)
cart1.add_goods("apple", 10)
print(cart1.get_goods())
print(cart1.get_summ())
cart1.remove_goods("apple", 10)
print(cart1.get_goods())
print(cart1.get_summ())