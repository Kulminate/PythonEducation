import math

class Table:
    def cntng_square(self):
        raise Exception("The method must be overridden by the inheritor")

class Rectangular_Table(Table):
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def cntng_square(self):
        return self.width * self.length

class Round_Table(Table):
    def __init__(self, radius: int):
        self.radius = radius

    def cntng_square(self):
        return 2 * math.pi * self.radius


table = Table()
rectangular_table = Rectangular_Table(4, 9)
print(rectangular_table.cntng_square())
round_table = Round_Table(10)
print(round_table.cntng_square())
print(table.cntng_square())