from Task2ClassSomeNumber import SomeNumber

if __name__ == "__main__":
    number = SomeNumber(2)

    print(type(number.getN()))
    print(type(number.setN()))
    number.print()
    print(number.isPositive())