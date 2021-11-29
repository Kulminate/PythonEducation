from SomeNumber import SomeNumber

class TestSomeNumber:
    def get(self):
        return SomeNumber().getN()

    def set(self):
        return SomeNumber().setN(-10)

    def isPos(self):
        return SomeNumber().isPositive()


test = TestSomeNumber()
print(test.get())
print(test.set())
print(test.isPos())
