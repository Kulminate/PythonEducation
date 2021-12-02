from SomeNumber import SomeNumber

if __name__ == "__main__":
    number = SomeNumber(-5)

    print(number.getN())
    print(type(number.setN(2)))
    number.print()
    print(number.isPositive())
