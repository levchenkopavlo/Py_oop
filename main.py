import math
# Завдання 3
# Створіть клас Book з атрибутами title (назва
# книги), author (автор) та genre (жанр). Додайте метод
# display_info, який виведе інформацію про книгу у
# вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # print(f"{self.radius ** 2 * 3.14}")
        return self.radius ** 2 * math.pi


circle1 = Circle(5)
print(f"{circle1.area()}")
