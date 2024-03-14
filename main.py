class Animals:
    def move(self):
        print('Рухається')

    def eat_food(self):
        print('їсть')


class Dogs(Animals):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


class Cats(Animals):
    pass


# створення екземпляру класу
my_dog = Dogs("Rex", 2, "bulldog")
# методи
# my_dog.eat_food()
# my_dog.move()
print(my_dog.name)

