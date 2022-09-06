class Car:

    def __init__(self, color="yellow", type="mazda", year=4):
        self.color = color
        self.type = type
        self.year = year

    def car_drive(self):
        print("Автомобиль заведен")


    def car_stop(self):
        print("Автомобиль заглушен")

    def car_year(self, year):
        self.year = year
        return self.year

    def car_type(self, type):
        self.type = type
        return self.type

    def car_color(self, color):
        self.color = color
        return self.color

one = Car()

one.car_drive()
one.car_stop()
print(f'{one.car_color("red")}, {one.car_type("mazda")}, {one.car_year(4)}')
