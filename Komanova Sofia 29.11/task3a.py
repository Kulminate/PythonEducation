
# 3а) Класс Currency для работы с денежными суммами.
# 	- Класс должен быть представлен двумя private полями:
# 			qty; для хранения значания суммы
# 			name; для хранения названия валюты ("грн", "руб", "$")
# 	Реализовать конструктор:
# 		- с двумя параметрами, которые принимает (qty: float, name: str);
# 	- Реализовать метод отображения суммы на экран print();
# 		Напр. в виде: 154.65руб // отображать не более 2 знаков после запятой
# 	- Реализовать операцию сравнения:
# 		def isEqual(self, Currency); // вернет true, если и значение и строка - совпадают
# 	- Реализовать методы:
#         def __add__(self, other): // метод сложения
# 			(если name отличается от текущего поля 'name', то сложение не производить,
# 			а вывести сообщение об ошибке ("Error: currency names are differ 'грн' - 'руб')
# 		def __sub__(self, other):// метод вычитания ...

class Currency:
    def __init__(self, qty: float, name: str):
        self.__qty =qty
        self.__name = name

    def print(self):
        print(f"{round(self.__qty, 2)}{self.__name}")

    def __eq__(self, other):
        if self.__name ==other.__name and self.__qty ==other.__qty:
            return True
        else: return False

    def __add__(self, other):
        if other.__name == self.__name:
            return f"{self.__qty + other.__qty}  {self.__name}"
        else: raise "Error: currency names are differ 'грн' - 'руб'"

    def __sub__(self, other):
        if other.__name == self.__name:
            return f"{self.__qty - other.__qty}  {self.__name}"
        else: raise "Error: currency names are differ 'грн' - 'руб'"

if __name__ == '__main__':
    a = Currency(3.432323, 'руб')
    b = Currency(3.4898, 'руб')
    с = Currency(3.432323, 'руб')
    a.print()
    print("true, если и значение и строка - совпадают: ", b == a)
    print("true, если и значение и строка - совпадают: ", с == a)
    print("метод сложения: ", a + b)
    print("метод вычитания: ", b - a)




