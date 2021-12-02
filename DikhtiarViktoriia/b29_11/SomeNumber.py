class SomeNumber:
    def __init__(self, n: int = 0):
        self.__n = n

    def getN(self) -> int:
        return self.__n

    def setN(self, n: int = 0) -> None:
        self.__n = n

    def print(self):
        print(f"Число: {self.n}")

    def isPositive(self) -> bool:
        if self.__n >= 0:
            return True
        else:
            return False