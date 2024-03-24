# Завдання 3
# Створіть клас для конвертування з метричної системи в
# англійську, та навпаки. Реалізуйте функціональність у вигляді
# статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.
class Metric_converter:
    __counter = 0

    @staticmethod
    def m_to_e(length):
        Metric_converter.__counter += 1
        result = length / 0.0254
        str_result = f"{length} метрів = "
        if result // 63360:
            str_result += f'{round(result // 63360)} миль '
            result = result % 63360
        if result // 36:
            str_result += f'{round(result // 36)} ярдів '
            result = result % 36
        if result // 12:
            str_result += f'{round(result // 12)} футів '
            result = result % 12
        str_result += f'{round(result, 3)} дюймів.'
        return str_result

    @staticmethod
    def e_to_m(length):
        Metric_converter.__counter += 1
        result = length * 0.0254
        str_result = f"{length} дюймів = "
        if result // 1000:
            str_result += f'{round(result // 1000)} кілометрів '
            result = result % 1000
        if result // 1:
            str_result += f'{round(result)} метрів '
            result = result % 1
        str_result += f'{round(result * 100, 3)} сантиметрів.'
        return str_result

    @staticmethod
    def get_counter():
        return Metric_converter.__counter


с2 = Metric_converter()

print(Metric_converter.m_to_e(2200))
print(Metric_converter.e_to_m(1))
print(Metric_converter.e_to_m(100000))

с3 = Metric_converter()
print(с2.e_to_m(1))
print(с3.e_to_m(1))
print(f'Кількість викликів конвертера: {Metric_converter.get_counter()}')
print(f'Кількість викликів конвертера: {с2.get_counter()}')
print(f'Кількість викликів конвертера: {с3.get_counter()}')
