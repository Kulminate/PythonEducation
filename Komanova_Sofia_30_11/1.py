# 1) Создайте базовый класс «Стол» и дочерние: «Прямоугольные столы» и «Круглые столы».
# В базовом классе должен быть метод вычисления площади поверхности стола, который будет переопределяться
# у наследников
# В базовом классе этот метод должен вызывать ошибку - что метод должен быть переопределен у наследника.
#
# Вычисления площади для прямоугольного – ширина и длина, для круглого – радиус. В дочерних классах реализуйте
# метод вычисления площади поверхности стола.
import math
class Table:
    def square(self):
        raise 'метод должен быть переопределен у наследника'

class Rectangle_table(Table):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.width * self.length

class Round_table(Table):

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * pow(self.radius,2)

if __name__== '__main__':
    # t0 = Table()
    # print(t0.square())
    t1 = Rectangle_table(2,3)
    print(t1.square())
    t2 = Round_table(2)
    print(t2.square())
