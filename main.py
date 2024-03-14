# Завдання 4
# До вже реалізованого класу «Книга» додайте
# необхідні перевантажені методи та оператори.

class Book:
    def __init__(self, tittle, author, genre, capacity):
        self.tittle = tittle
        self.author = author
        self.genre = genre
        self.capacity = capacity

          jk    def __str__(self):
        return f"Назва: {self.tittle}\nАвтор: {self.author}\nЖанр: {self.genre}"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __abs__(self):
        return f"ABS function is unlocked"

    def start_engine(self):
        print(f"Двигун {self.brand} {self.model} запущено")


book1 = Book("Гарі Поттер","Джоан Роулінг", "фентезі")
book1.display_info()
