# Завдання 3
# Створіть клас Book з атрибутами title (назва
# книги), author (автор) та genre (жанр). Додайте метод
# display_info, який виведе інформацію про книгу у
# вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".

class Book:
    def __init__(self, tittle, author, genre):
        self.tittle = tittle
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.tittle}, Автор: {self.author}, Жанр: {self.genre}")


book1 = Book("Гарі Поттер","Джоан Роулінг", "фентезі")
book1.display_info()
