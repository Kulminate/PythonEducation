class Currency:
    def __init__(self, qty: float, name: str):
        self.__qty = qty
        self.__name = name

    def print(self):
        print(f"{round(self.__qty, 2)}{self.__name}")

    def isEqual(self, Currency):
        if self.__qty == Currency.__qty and self.__name == Currency.__name:
            return True
        else:
            return False

    def __add__(self, other):
        if self.__name == other.__name:
            return self.__qty + other.__qty
        else:
            raise Exception("Error: currency names are differ 'грн' - 'руб'")

    def __sub__(self, other):
        if self.__name == other.__name:
            return self.__qty - other.__qty
        else:
            raise Exception("Error: currency names are differ 'грн' - 'руб")
