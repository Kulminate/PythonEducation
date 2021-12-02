from math import pi


class Table:
    def __init__(self, a=None, b=None) -> None:
        self.a = a
        self.b = b
    def square_finder(self):
        raise Exception("Method should be defined with a Child class")


class RoundTables(Table):

    def __init__(self, r):
        self.r = r

    def square_finder(self):
        try:
            return round(int(self.r)**2*pi, 2)
        except(ValueError, UnboundLocalError, TypeError):
            raise ValueError("The given data is wrong")


class RectangleTables(Table):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square_finder(self):
        try:
            return int(self.a)*int(self.b)
        except(ValueError, UnboundLocalError, TypeError):
            raise ValueError("The given data is wrong")
