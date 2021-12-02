from SomeNumber import SomeNumber

class TestSomeNumber:
    def __init__(self, num):
        self.num = num

    def test(self):
        for i in self.num:
            print(SomeNumber(i).getN())
            print(SomeNumber(i).setN(i))
            print(SomeNumber(i).isPositive())



if __name__ == "__main__":

    t = TestSomeNumber([-10, -1, 0, 1, 15])
    print(t.test())
