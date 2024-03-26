class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self._student_id = student_id

    def get_id(self):
        return self._student_id

    def set_id(self, new_id):
        self._student_id = new_id

    def get_info(self, objects):
        print(f'Студент {self._name} вивчає')

        print(list(enumerate(objects)))
        for i, object in enumerate(objects):
            print(f'{i+1}. {object}')


student = Student('john', 27, 'male', '0454345')
student.get_info(['qw','as','zx'])