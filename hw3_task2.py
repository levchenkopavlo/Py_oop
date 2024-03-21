# Завдання 2
# Розробіть систему управління замовленнями таксі.
# Кожне замовлення має містити інформацію про
# клієнта, адресу, тип автомобіля та вартість. Реалізуйте
# методи для додавання нових замовлень, зміни адреси та
# типу автомобіля, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від
# неправильних змін.
class Taxi_orders:
    def __init__(self, name=None, address=None, car_type=None, cost=None):
        self.__name = name
        self.__address = address
        self.__car_type = car_type
        self.__cost = cost

    def __str__(self):
        return f'{self.__name},{self.__address},{self.__car_type},{self.__cost}'

    def input(self):
        while True:
            self.__name = input("Введіть ім'я клієнта: ")
            self.__address = input("Введіть адресу: ")
            self.__car_type = input("Введіть тип автомобіля: ")
            cost = input("Введіть вартість: ")
            if self.__name == "" or self.__address == "" or self.__car_type == "" or not cost.isdigit():
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                self.__cost = int(cost)
                break

    def show(self):
        return f"Ім'я: {self.__name};\nАдреса: {self.__address};\nТип автомобіля: {self.__car_type};\nВартість: {self.__cost}."

    def set_address(self, address):
        self.__address = address

    def set_car_type(self, car_type):
        self.__car_type = car_type

    def set_cost(self, cost):
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_car_type(self):
        return self.__car_type

    def get_cost(self):
        return self.__cost


order1 = Taxi_orders()
print(order1.__str__())
order1.input()
print(order1.show())
order1.set_car_type("lux")
print(order1.show())
del order1
