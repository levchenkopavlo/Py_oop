import math


# Завдання 3
# Створіть клас для підрахунку максимуму з чотирьох
# аргументів, мінімуму з чотирьох аргументів, середнє
# арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
# методів.
class MinMax:
    @staticmethod
    def get_max(*args):
        return max(args)

    @staticmethod
    def get_min(*args):
        return min(args)

    @staticmethod
    def get_avg(*args):
        return sum(args) / len(args)

    @staticmethod
    def get_fact(*args):
        res = [math.factorial(i) for i in args]
        return ', '.join(map(str, res))


print(MinMax.get_max(3, 6, 5, 2))
print(MinMax.get_avg(4, 6))
print(MinMax.get_fact(4, 6))
