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
#               def __add__(self, other): // метод сложения
# 			(если name отличается от текущего поля 'name', то сложение не производить,
# 			а вывести сообщение об ошибке ("Error: currency names are differ 'грн' - 'руб')
# 		def __sub__(self, other):// метод вычитания ...

from Currency import Currency

if __name__ == "__main__":
    curr1 = Currency(150.669, "грн")
    curr2 = Currency(350.876, "руб")

    curr1.print()
    curr2.print()
    print()

    print(curr1.isEqual(curr2))
    print(curr1.isEqual(curr1), "\n")

    print(curr1 + curr2)
    print(curr1 + curr1, "\n")

    print(curr1 - curr2)
    print(curr2 - curr2)
