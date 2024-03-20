# Завдання 1
# Створіть систему управління замовленнями
# готелю. Кожне замовлення має містити інформацію
# про клієнта, тип кімнати, кількість днів проживання та
# вартість. Реалізуйте методи для додавання замовлення,
# зміни типу кімнати та кількості днів, а також
# видалення замовлення. Використайте інкапсуляцію для
# захисту вартості від неправильних змін.
class Booking:
    def __init__(self, name=None, room_type=None, days=None, cost=None):
        self.__name = name
        self.__room_type = room_type
        self.__days = days
        self.__cost = cost

    def __str__(self):
        return f'{self.__name},{self.__room_type},{self.__days},{self.__cost}'

    def input(self):
        while True:
            self.__name = input("Введіть ім'я клієнта: ")
            self.__room_type = input("Введіть тип кімнати: ")
            days = input("Введіть кількість днів: ")
            cost = input("Введіть вартість: ")
            if self.__name == "" or self.__room_type == "" or not days.isdigit() or not cost.isdigit():
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                self.__days = int(days)
                self.__cost = int(cost)
                break

    def show(self):
        return f"Ім'я: {self.__name};\nТип кімнати: {self.__room_type};\nДнів: {self.__days};\nВартість: {self.__cost}."

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def set_days(self, days):
        self.__days = days

    def set_cost(self, cost):
        self.__cost = cost

booking1 = Booking()
print(booking1.__str__())
booking1.input()
print(booking1.show())
booking1.set_days(8)
print(booking1.show())
del booking1
# if booking1:
#     print(booking1.show())
# else:
#     print("елемент не знайдено")