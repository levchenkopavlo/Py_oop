# Завдання 1
# Використовуючи поняття множинного успадкування,
# створіть клас «Коло, поміщене в квадрат».
class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'{self.__dict__}'


class Circle:
    def __init__(self, radius):
        self.radius = radius


class Circle_in_Square(Square, Circle):
    def __init__(self, side, radius):
        Square.__init__(self, side)
        Circle.__init__(self, radius)

    def info(self):
        print(f'side: {self.side}, radius: {self.radius}')


circleInSquare1 = Circle_in_Square(4, 2)
print(circleInSquare1)
circleInSquare1.info()
