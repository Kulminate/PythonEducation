class SomeNumber:

    def __init__(self, n: int = 0):
        self.n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        self.__n = n

    def getN(self) -> int:
        return int(self.__n)

    def setN(self, number) -> None:
        self.__n = number

    def print(self):
        return print(f'Number is {self.__n}')

    def isPositive(self) -> bool:
        if self.__n > 0:
            return True
        elif self.__n < 0:
            return False
        elif self.__n == 0:
            return None

