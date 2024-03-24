# Завдання 2
# Створіть клас для конвертування температури з Цельсія
# у Фаренгейт, і навпаки. У класі має знаходитися два статичні
# методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
# кількість підрахунків температури та повернути це значення
# статичним методом.
class CF_converter:
    __counter = 0

    @staticmethod
    def get_counter():
        return CF_converter.__counter

    @staticmethod
    def c_to_f(c):
        CF_converter.__counter += 1
        return c * 9 / 5 + 32

    @staticmethod
    def f_to_c(f):
        CF_converter.__counter += 1
        return (f - 32) * 5 / 9


print(CF_converter.c_to_f(0))
print(CF_converter.f_to_c(32))
print(CF_converter.get_counter())