#) Создайте базовый класс «Стол» и дочерние: «Прямоугольные столы» и «Круглые столы».
#В базовом классе должен быть метод вычисления площади поверхности стола, который будет переопределяться у наследников
#В базовом классе этот метод должен вызывать ошибку - что метод должен быть переопределен у наследника.
#Вычисления площади для прямоугольного – ширина и длина, для круглого – радиус.
# В дочерних классах реализуйте метод вычисления площади поверхности стола.

from math import pi

class Table:

    def getSuare(self) -> float:
        raise Exception ("This method must be overridden")


class RectangularTable(Table):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def getSuare(self) -> float:
        return self.width * self.height


class RoundTable(Table):

    def __init__(self, radius: float):
        self.radius = radius

    def getSuare(self) -> float:
        return self.radius * self.radius * pi

rectangularTable = RectangularTable(10, 20)
roundTable = RoundTable(5)
print(f"Square of rectangular table is {rectangularTable.getSuare()}")
print(f"Square of round table is {roundTable.getSuare()}")
