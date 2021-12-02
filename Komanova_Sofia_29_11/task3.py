# 3) Создайте класс TestSomeNumber, в котором продемонстрируйте работу класса SomeNumber
# 		на нескольких тестовых данных [-10, -1, 0, 1, 15]
# 	a) проверить работу конструкторов
# 	b) проверить работу метода setN();
# 	c) проверить работу метода isPositive();


from task2 import SomeNumber

class TestSomeNumber:
    def __init__(self, *test_date):
        self.date = test_date

    def test(self):
        for i in self.date:
            print(f"Проверка числа {i}")
            some_num = SomeNumber()
            print(f'Проверка работы конструктора:  {some_num.num}')
            some_num.num = i
            print(f'Проверка работы setN():  {some_num.num}')
            print("Проверка работы метода isPositive()")
            some_num.isPositive()



if __name__ == '__main__':
    data = TestSomeNumber(-10, -1, 0, 1, 15)
    data.test()





