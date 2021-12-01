import math

class Table:
    def calc_square(self):
        raise Exception("Метод должен быть переопределен у наследника!")

class Rectangular_Table(Table):
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def calc_square(self):
        return self.width * self.length

class Round_Table(Table):
    def __init__(self, radius: int):
        self.radius = radius

    def calc_square(self):
        return 2 * math.pi * self.radius


table = Table()
rectangular_table = Rectangular_Table(10, 20)
print(rectangular_table.calc_square())
round_table = Round_Table(10)
print(round_table.calc_square())
print(table.calc_square())