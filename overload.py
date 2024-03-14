# перевантаження методів
class StringManipulator:
    def concat(self, a, b):
        return a + b

    def concat(self, a, b):
        return str(a + b)


calc = StringManipulator()
print(calc.concat(2, 3))
print(calc.concat("qwe", "rty"))
