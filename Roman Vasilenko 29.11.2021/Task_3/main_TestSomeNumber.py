from SomeNumber import SomeNumber
from TestSomeNumber import TestSomeNumber

if __name__ == '__main__':
    # Объект создается == конструктор работает
    number = SomeNumber(5)
    print(number)

    TestSomeNumber.test_setN()
    TestSomeNumber.test_is_positive()
