# 2) Предположим, имеется следующий класс.
# 	class SomeNumber:
# 		self.n # единственное поле класса
#         a) Конструктор, с одним параметром (int n, по умолчанию инициализируем 0)
# 	b) Метод def getN() -> int;
# 	c) Метод def setN() -> None;
# 	d) Метод print();
# 			который выводит строку, напр: "Число: 5"
# 	e) Метод isPositive() -> boolean; // которые возвращает true,
# 	если число положительное и false, если число отрицательное

class SomeNumber:

    def __init__(self, n: int) -> None:
        self.n = n

    @property
    def n(self) -> int:
        return self.__n

    @n.setter
    def n(self, n: int) -> None:
        self.__n = n

    def isPositive(self) -> bool:
        if self.n != 0:
            return self.n > 0
        else:
            print("Ноль не позитивное и не негативное число")
            return False

    def print(self) -> None:
        print(f'Число: {self.n}')
