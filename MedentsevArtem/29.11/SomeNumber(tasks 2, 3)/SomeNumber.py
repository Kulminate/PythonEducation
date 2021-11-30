# 2) Предположим, имеется следующий класс.
# 	class SomeNumber:
# 		self.n # единственное поле класса
#         a) Конструктор, с одним параметром (int n, по умолчанию инициализируем 0)
# 	b) Метод def getN() -> int;
# 	c) Метод def setN() -> None;
# 	d) Метод print();
# 			который выводит строку, напр: "Число: 5"
# 	e) Метод isPositive() -> boolean; // которые возвращает true, если число
# 	положительное и false, если число отрицательное
class SomeNumber():

    def __init__(self, n=0) -> int:
        self._n = n

    def getN(self) -> int:
        return self._n

    def setN(self, n: int) -> None:
        self._n = n

    def print(self):
        print('Число:', self._n)

    def isPositive(self) -> bool:
        if self._n > 0:
            return True
        elif self._n == 0:
            return None
        else:
            return False

# a = SomeNumber(-1)
# print(a.isPositive())
