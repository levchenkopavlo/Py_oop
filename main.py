import re


# Завдання 5
# Реалізуйте клас «Вебсайт». Збережіть у класі: назву
# вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
# та методи класу для введення-виведення даних, а також
# для інших операцій. Використовуйте механізм переван таження методів.
class Site:
    def __init__(self, name="", url="", description=""):
        self.name = name
        self.url = url
        self.description = description

    def input_data(self):
        while True:
            self.name = input("Введіть назву сайту: ")
            url = input("Введіть адресу: ")
            self.description = input("Введіть короткий опис сайту: ")
            pattern = r'^https?://(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}$'
            if self.name == "" or self.url == "" or not re.search(pattern, url):
                print("Помилка вводу даних. Введіть знову.")
                continue
            else:
                self.url = url
                break

    def __str__(self):
        return [self.name, self.url, self.description]

    def show(self):
        return f"Назва сайту: {self.name};\nАдреса: {self.url};\nОпис: {self.description}."

    def __eq__(self, other):
        return self.url == other.url

    def __lt__(self, other):
        return len(self.url) < len(other.url)

    def __gt__(self, other):
        return len(self.url) > len(other.url)

    def __ne__(self, other):
        return self.url != other.url
