class UIelement:
    def __init__(self, functionality):
        self.functionality = functionality

    def display(self):
        print('display UIelement')

class InteractiveElement:
    def click(self):
        print('click')

class Button(UIelement):
    def __init__(self, functionality, label):
        super().__init__(functionality)
        self.label = label

    def display(self):
        print('display Button')


class Menu(UIelement):
    def __init__(self,functionality,info):
        super().__init__(functionality)
        self.info = info
    def display(self):
        print('display Menu')


class FieldInput(UIelement, InteractiveElement):
    def display(self):
        print('display FieldInput')

button=Button()