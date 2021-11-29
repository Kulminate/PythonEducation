# 3) Создайте класс TestSomeNumber, в котором продемонстрируйте работу класса SomeNumber
# 		на нескольких тестовых данных [-10, -1, 0, 1, 15]
# 	a) проверить работу конструкторов
# 	b) проверить работу метода setN();
# 	c) проверить работу метода isPositive();


from task2 import SomeNumber

class TestSomeNumber:
    if __name__ == '__main__':
        d = SomeNumber() #проверить работу конструкторов
        print("d:", d.num)
        a = SomeNumber(-10)
        print("a:", a.num)
        c = SomeNumber()
        c.num = -1 #проверить работу метода setN()
        print("c:", c.num)
        e = SomeNumber(1)
        print("e:", e.num)
        f = SomeNumber(15)
        print("f:", f.num)
        f.isPositive() # проверить работу метода isPositive();
        c.isPositive()
        d.isPositive()




