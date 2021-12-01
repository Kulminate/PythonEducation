# Предположим, имеется следующий класс.
# class SomeNumber:
# 	self.n # единственное поле класса
#        a) Конструктор, с одним параметром (int n, по умолчанию инициализируем 0)
# b) Метод def getN() -> int;
# c) Метод def setN() -> None;
# d) Метод print();
# 		который выводит строку, напр: "Число: 5"
# e) Метод isPositive() -> boolean; // которые возвращает true,
# если число положительное и false, если число отрицательное

class SomeNumber:
    def __init__(self, n: int = 0):
        self.__n = n

    @property
    def num(self):
        return self.__n

    @num.setter
    def num(self, new_n: int):
        try:
            self.__n = int(new_n)
        except ValueError as e:
            print(e)

    def print(self):
        print(f"Число: {self.__n}")

    def isPositive(self):
        if self.__n > 0:
            return True
        elif self.__n == 0:
            print("Число равно нулю")
        else:
            return False
