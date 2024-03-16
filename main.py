# Завдання 4
# До вже реалізованого класу «Книга» додайте
# необхідні перевантажені методи та оператори.

class Book:
    def __init__(self, tittle="", author="", genre="", year=None, capacity=0):
        self.tittle = tittle
        self.author = author
        self.genre = genre
        self.capacity = capacity
        self.year = year

    def input_data(self):
        self.tittle = input("Введіть назву книги: ")
        self.author = input("Введіть автора: ")
        self.genre = input("Введіть жанр: ")
        self.year = int(input("Введіть рік випуску: "))
        self.capacity = int(input("Введіть кількість сторінок: "))

    def __str__(self):
        return [self.tittle, self.author, self.genre, self.year, self.capacity]

    def show(self):
        return f"Назва: {self.tittle};\nАвтор: {self.author};\nЖанр: {self.genre};\nYear: {self.year};\nСторінок: {self.capacity}."

    def __eq__(self, other):
        return self.tittle == other.tittle and self.author == other.author

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __ne__(self, other):
        return self.tittle != other.tittle or self.author != other.author


book1 = Book("Гарі Поттер і філософський камінь", "Джоан Роулінг", "фентезі", 1997, 550)
book2 = Book("Чужак", "Макс Фрай", "фентезі", 1996, 420)
print(book1.show())
print(book1.__str__())
print(book2.__str__())
print(book1==book2)