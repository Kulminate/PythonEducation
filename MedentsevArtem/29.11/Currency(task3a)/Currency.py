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
class Currency():
    def __init__(self, qty, name):
        self.qty = qty
        self.name = name

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty) -> None:
        try:
            self.__qty = float(qty)
        except(ValueError, UnboundLocalError, TypeError):
            raise ValueError("Invalid data.")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if name == "грн" or name == "руб" or name == "$":
            self.__name = str(name)
        else:
            raise ValueError('Wrong data format.')

    def print(self):
        print(round(self.qty, 2), self.name, sep='')

    def isEqual(self, Currency):
        if self.__name == Currency:
            return True
        else:
            return False

    def __add__(self, other):
        if self.__name == other.__name:
            return f"{self.__qty + other.__qty} {self.name}"
        else:
            raise ValueError(f"Error: currency names are differ \'{self.__name}\' - \'{other.__name}\'")

    def __sub__(self, other):
        if self.__name == other.__name:
            return f"{self.__qty - other.__qty} {self.name}"
        else:
            raise ValueError(f"Error: currency names are differ \'{self.__name}\' - \'{other.__name}\'")