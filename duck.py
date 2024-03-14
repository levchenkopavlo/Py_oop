# качина типізація
class Duck:
    def quack(self):
        print("Кряк!")


class Person:
    def quack(self):
        print("Крякає по людськи!")


def make_it_quack(obj):
    obj.quack()


duck = Duck()
person = Person()
make_it_quack(duck)
make_it_quack(person)
