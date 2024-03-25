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
        # str_result = f"{length} метрів = "
        str_result = f""
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
        # str_result = f"{length} дюймів = "
        str_result = f""
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


measure = {'1': 'кілометрах', '2': 'метрах', '3': 'сантиметрах', '4': 'милях', '5': 'ярдах', '6': 'футах',
           '7': 'дюймах'}
while True:
    print(f"\033[33m1\033[0m. Конвертувати кілометри")
    print(f"\033[33m2\033[0m. Конвертувати метри")
    print(f"\033[33m3\033[0m. Конвертувати сантиметри")
    print(f"\033[33m4\033[0m. Конвертувати милі")
    print(f"\033[33m5\033[0m. Конвертувати ярди")
    print(f"\033[33m6\033[0m. Конвертувати фути")
    print(f"\033[33m7\033[0m. Конвертувати дюйми")
    userChoice = input("Виберіть необхідний пункт меню (Enter для виходу): ")
    if userChoice.isdigit():
        if 0 < int(userChoice) < 8:
            length = input(f"Введіть довжину в {measure[userChoice]}: ")
            if length.replace('.', '', 1).isdigit():
                length_d = float(length)
                match userChoice:
                    case "1":
                        print(Metric_converter.m_to_e(length_d * 1000))
                    case "2":
                        print(Metric_converter.m_to_e(length_d))
                    case "3":
                        print(Metric_converter.m_to_e(length_d / 100))
                    case "4":
                        print(Metric_converter.e_to_m(length_d * 63360))
                    case "5":
                        print(Metric_converter.e_to_m(length_d * 36))
                    case "6":
                        print(Metric_converter.e_to_m(length_d * 12))
                    case "7":
                        print(Metric_converter.e_to_m(length_d))

        else:
            continue
    elif userChoice == '':
        break
    else:
        continue
print(f'Кількість викликів конвертера: {Metric_converter.get_counter()}')
