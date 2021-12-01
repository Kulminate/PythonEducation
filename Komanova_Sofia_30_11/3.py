# 3) В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения.
# Для его перегрузки используется метод __add__(). Он вызывается, когда объекты класса, имеющего д
# анный метод, фигурируют в операции сложения, причем с левой стороны. Это значит, что в выражении a + b у
# объекта a должен быть метод __add__(). Объект b может быть чем угодно, но чаще всего он бывает объектом
# того же класса. Объект b будет автоматически передаваться в метод __add__() в качестве второго аргумента
# (первый – self).

class Add:
    def __init__(self, a:int, b:str):
        self.__a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @ a.setter
    def a(self, a):
        self.__a = a

    def __add__(self, other):
        return f"{self.__a + other.__a} {self.b + other.b}"

if __name__ == '__main__':
    num1 = Add(2,'sadad')
    num2 = Add(3,'HEY')
    print(num1+num2)

