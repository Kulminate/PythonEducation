class SomeNumber:

    def __init__(self, n: int = 0):
        self.n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        self.__n = n

    def getN(self):
        return int(self.__n)

    def setN(self):
        return None

    def print(self):
        return print(f'Number is {self.__n}')

    def isPositive(self):
        if self.__n > 0:
            return f'Number {self.__n} is positive'
        elif self.__n < 0:
            return f'Number {self.__n} is negative'
        elif self.__n == 0:
            return f'Number {self.__n} is null'
