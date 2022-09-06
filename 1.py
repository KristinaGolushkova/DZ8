class Student:

    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.group_number = group_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name_age(self, name, age):
        self.name = name
        self.age = age
        return f'{self.name}, {self.age}'

    def set_group_number(self, group_number):
        self.group_number = group_number
        return f' {self.get_group_number()}.'


Stepan= Student("Stepan", 20, "1б")
Vova = Student("Vova", 19, "3h")
Ivan = Student()
Mila = Student()
Sasha = Student("Sasha", 19, "11v")
print(f'{Stepan.get_name()}, {Stepan.get_age()}, {Stepan.get_group_number()}')
print(f'{Vova.get_name()}, {Vova.get_age()}, {Vova.get_group_number()}')
print(f'{Ivan.name}, {Ivan.age}, {Ivan.group_number}.')
print(f'{Sasha.get_name()}, {Sasha.get_age()}, {Sasha.get_group_number()}')
print(f'{Mila.set_name_age("Maya", 25)}, {Mila.set_group_number("16b")}')