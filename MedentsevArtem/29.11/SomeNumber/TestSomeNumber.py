from SomeNumber import SomeNumber


class TestSomeNumber():
    def __init__(self, var):
        self.var = var

    def test(self):
        for i in self.var:
            t = SomeNumber(i)
            print(t.isPositive())
        for i in self.var:
            t = SomeNumber(i)
            print(t.getN())
        for i in self.var:
            t = SomeNumber(i)
            print(t.setN())
        return 'Test is ended.'


if __name__ == "__main__":
    a = TestSomeNumber([-10, -1, 0, 1, 15])
    print(a.test())

