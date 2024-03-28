class CPU:
    def __init__(self, num_kernel):
        print('print init CPU')
        self.kernel = num_kernel


class GPU:
    def __init__(self, memory):
        print('print init GPU')
        self.memory = memory


class RAM:
    def __init__(self, capacity):
        print('print init RAM')
        self.capacity = capacity


class Motherboard:
    def __init__(self, socket):
        print('print init Motherboard')
        self.socket = socket


class Computer(CPU, GPU, RAM, Motherboard):
    def __init__(self, num_kernel, memory, capacity, socket):
        print(f'print init from {self.__class__.__name__}')
        super().__init__(num_kernel)
        GPU.__init__(self, memory)
        RAM.__init__(self, capacity)
        Motherboard.__init__(self, socket)

