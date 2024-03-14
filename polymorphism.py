# статичний поліморфізм
def add(x, y):
    return x + y


result1 = add(1, 4)
result2 = add("Hello", " python")
print(result1)
print(result2)


# динамічний поліморфізм
class Animals:
    def move(self):
        print('Рухається')


class Dog(Animals):
    def make_sound(self):
        return "Woof"


class Cat(Animals):
    def make_sound(self):
        return "Meow"


def animal_speak():
    pass


dog, cat = Dog(), Cat()
