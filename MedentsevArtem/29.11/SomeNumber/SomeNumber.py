class SomeNumber():

    def __init__(self, n=0):
        self.n = int(n)

    def getN(self) -> int:
        return int(self.n)

    def setN(self) -> None:
        return None

    def print(self):
        print('Число:', self.n)

    def isPositive(self) -> bool:
        if self.n > 0:
            return True
        elif self.n == 0:
            return None
        else:
            return False

# a = SomeNumber(-1)
# print(a.isPositive())
