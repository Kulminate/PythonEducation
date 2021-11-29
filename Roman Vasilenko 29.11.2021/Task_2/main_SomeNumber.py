from SomeNumber import SomeNumber

if __name__ == "__main__":
    number = SomeNumber(-5)

    print(type(number.getN()))
    print(type(number.setN()))
    number.print()
    print(number.isPositive())
