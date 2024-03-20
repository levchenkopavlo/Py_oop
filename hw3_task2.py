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
            if self.__name == "" or self.__address == "" or self.__car_type or not cost.isdigit():
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                self.__cost = int(cost)
                break

    def show(self):
        return f"Ім'я: {self.__name};\nТип кімнати: {self.__address};\nДнів: {self.__car_type};\nВартість: {self.__cost}."

    def set_room_type(self, room_type):
        self.__address = room_type

    def set_days(self, days):
        self.__car_type = days

    def set_cost(self, cost):
        self.__cost = cost

booking1 = Taxi_orders()
print(booking1.__str__())
booking1.input()
print(booking1.show())
booking1.set_days(8)
print(booking1.show())
del booking1