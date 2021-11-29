# 3) Создайте класс TestSomeNumber, в котором продемонстрируйте работу класса SomeNumber
# 		на нескольких тестовых данных [-10, -1, 0, 1, 15]
# 	a) проверить работу конструкторов
# 	b) проверить работу метода setN();
# 	c) проверить работу метода isPositive();
from SomeNumber import SomeNumber


class TestSomeNumber:
    def __init__(self, test_set=[-10, -1, 0, 1, 15]):
        self.test_set = test_set

    @staticmethod
    def test():
        # for num in test_set:
        for num in [-10, -1, 0, 1, 15]:
            print(f"Тестируем SomeNumber на числе {num}:")

            some_num = SomeNumber(num)
            if some_num.n == num:
                print("Конструктор работает корректно")
            else:
                print("Конструктор работает некорректно")

            some_num.print()


            some_num.n = num
            if some_num.n == num:
                print("Функция setter работает корректно")
            else:
                print("Функция setter работает некорректно")

            if some_num.isPositive() == num > 0:
                print(f'test = {num > 0}')
                print("Функция isPositive работает корректно\n")
            else:
                print("Функция isPositive работает некорректно\n")
