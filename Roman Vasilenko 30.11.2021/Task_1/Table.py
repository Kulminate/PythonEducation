import math


class Table:

    number_legs = 4

    def square(self):
        raise Exception('square() method must be redefined')


class RectTable(Table):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, length):
        self._length = length

    @width.setter
    def width(self, width):
        self._width = width

    def square(self) -> int:
        print(f'Square is {self._width * self._length}')
        return self._width * self._length


class RoundTable(Table):

    def __init__(self, table_radius):
        self.table_radius = table_radius

    @property
    def table_radius(self):
        return self._table_radius

    @table_radius.setter
    def table_radius(self, table_radius):
        self._table_radius = table_radius

    def square(self) -> float:
        square = math.pi * math.pow(self.table_radius, 2)
        print(f'Square is {round(square, 3)}')
        return round(square, 4)