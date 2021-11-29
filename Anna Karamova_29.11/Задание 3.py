# Задание 3) Создайте класс TestSomeNumber, в котором продемонстрируйте работу класса SomeNumber
#		на нескольких тестовых данных [-10, -1, 0, 1, 15]
#	a) проверить работу конструкторов
#	b) проверить работу метода setN();
#	c) проверить работу метода isPositive();

from SomeNumber import SomeNumber

class TestSomeNumber:
    @staticmethod
    def print_result(description, result):
        print(description, "пройден" if result else "не пройден")

    @staticmethod
    def test_constructor():
        print("Тест конструктора:")
        for num in [-10, -1, 0, 1, 15] :
            someNumber = SomeNumber(num)
            test_passed = someNumber.getN() == num
            TestSomeNumber.print_result(f"{num} = {num}", test_passed)
        print()

    @staticmethod
    def test_setN():
        print("Тест метода setN:")
        someNumber = SomeNumber()
        for num in [-10, -1, 0, 1, 15] :
            someNumber.setN(num)
            test_passed = someNumber.getN() == num
            TestSomeNumber.print_result(f"setN({num}) = {num}", test_passed)
        print()

    @staticmethod
    def test_isPositive():
        print("Тест метода isPositive():")

        for num in [-10, -1, 0, 1, 15] :
            someNumber = SomeNumber(num)
            test_passed = someNumber.isPositive() == (num > 0)
            TestSomeNumber.print_result(f"{num} isPositive = {num > 0}", test_passed)
        print()

TestSomeNumber.test_constructor()
TestSomeNumber.test_setN()
TestSomeNumber.test_isPositive()


