# Завдання 4
# Створіть клас "Комп'ютер", який має зберігати
# інформацію про процесор, ОЗУ та відеокарту. Застосуйте
# інкапсуляцію для захисту цих даних від змін.
class Computer:
    def __init__(self, cpu="", ram="", gpu=""):
        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu

    def __str__(self):
        return [self.__cpu, self.__ram, self.__gpu]

    def info(self):
        return f'CPU: {self.__cpu};RAM: {self.__ram};GPU: {self.__gpu}.'

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_ram(self, ram):
        self.__ram = ram

    def set_gpu(self, gpu):
        self.__gpu = gpu

    def get_cpu(self):
        return self.__cpu

    def get_ram(self):
        return self.__ram

    def get_gpu(self):
        return self.__gpu


computer1 = Computer()
computer1.set_cpu("Intel G2020")
computer1.set_ram("Goodram 8Gb")
computer1.set_gpu("Intel integrated")

print(computer1.get_cpu())
print(computer1.info())
print(computer1.__str__())
