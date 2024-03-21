# Завдання 4
# Створіть клас FileUtils, який має метод класу
# count_lines, який приймає шлях до файлу і повертає
# кількість рядків у файлі.

class FileUtils:
    @staticmethod
    def count_lines(path):
        try:
            with open(path, "r", encoding="utf-8") as fileToRead:
                data = fileToRead.readlines()
                return len(data)
        except Exception as e:
            print(e)


print(FileUtils.count_lines("text_file1.txt"))