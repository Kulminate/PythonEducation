# Создайте класс TestSomeNumber, в котором продемонстрируйте работу класса SomeNumber
# 	на нескольких тестовых данных [-10, -1, 0, 1, 15]
# a) проверить работу конструкторов
# b) проверить работу метода setN();
# c) проверить работу метода isPositive();

from Task2 import SomeNumber

class TestSomeNumber:
    if __name__ == '__main__':

        d = SomeNumber()        #проверяем работу конструкторов
        print("d:", d.number)

        a = SomeNumber(-10)
        print("a:", a.number)
        c = SomeNumber(-1)      # работа метода setN()
        print("c:", c.number)
        e = SomeNumber(1)
        print("e:", e.number)
        f = SomeNumber(15)
        print("f:", f.number)

        print(f.isPositive())    # работа метода isPositive();
        print(c.isPositive())
        d.isPositive()

