# Задание 2
# Предположим, имеется следующий класс.
#	class SomeNumber
#		self.n # единственное поле класса
#	a) Конструктор, с одним параметром (int n, по умолчанию инициализируем 0)
#	b) Метод def getN() -> int;
#	c) Метод def setN() -> None;
#   d) Метод print();
# 			который выводит строку, напр: "Число: 5"
#	e) ММетод isPositive() -> boolean; // которые возвращает true, если число положительное и false,
#	если число отрицательное

class SomeNumber:
    def __init__(self, n=0):
        self.setN(n)

    def getN(self):
        return self.__n

    def setN(self, number):
        self.__n = number

    def print(self):
        print(f"Число {self.__n}")

    def isPositive(self):
        return self.__n > 0


sn = SomeNumber(-10)
sn.print()
print("положительное" if sn.isPositive() else "отрицательное")