# 3) Создайте класс TestSomeNumber, в котором продемонстрируйте работу класса SomeNumber
# 		на нескольких тестовых данных [-10, -1, 0, 1, 15]
# 	a) проверить работу конструкторов
# 	b) проверить работу метода setN();
# 	c) проверить работу метода isPositive();
from SomeNumber import SomeNumber


class TestSomeNumber:
    def __init__(self):
        pass

    @staticmethod
    def test():
        test_set = [-10, -1, 0, 1, 15]
        print(f"Тестируем SomeNumber:\n")
        for num in test_set:

            some_num = SomeNumber(num)
            some_num.print()
            if some_num.n == num:
                print("Конструктор работает корректно")
            else:
                print("Конструктор работает некорректно")

            some_num.n = num
            if some_num.n == num:
                print("Функция setter работает корректно")
            else:
                print("Функция setter работает некорректно")

            meth_val = some_num.isPositive()
            test_val = num > 0
            if meth_val == test_val:
                print("Функция isPositive работает корректно\n")
            else:
                print("Функция isPositive работает некорректно\n")
