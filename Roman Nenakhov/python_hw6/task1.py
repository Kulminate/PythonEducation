# Создайте базовый класс «Стол» и дочерние:
# «Прямоугольные столы» и «Круглые столы».
# В базовом классе должен быть метод вычисления площади
# поверхности стола, который будет переопределяться у наследников
# В базовом классе этот метод должен вызывать ошибку - что
# метод должен быть переопределен у наследника.
#
# Вычисления площади для прямоугольного – ширина и длина, для круглого – радиус.
# В дочерних классах реализуйте метод вычисления площади поверхности стола.
import math


class Table:

    def square(self):
        raise Exception('Method must be overridden in the descendant')


class RectangularTables(Table):

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
        return self._width * self._length


class RoundTables(Table):

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
        return round(square, 3)


if __name__ == '__main__':

    # table = Table()
    # table.square()

    rect_table = RectangularTables(length=6, width=5)
    print('Square of the rectangular table:  ', rect_table.square())

    round_table = RoundTables(4)
    print('Square of the round table ', round_table.square())
