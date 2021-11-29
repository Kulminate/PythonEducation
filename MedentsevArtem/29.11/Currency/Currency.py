class Currency():
    def __init__(self, qty, name):
        self.qty = qty
        self.name = name

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        self.__qty = float(qty)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
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
            return self.__qty + other.__qty
        else:
            raise ValueError(f"Error: currency names are differ \'{self.__name}\' - \'{other.__name}\'")

    def __sub__(self, other):
        if self.__name == other.__name:
            return self.__qty - other.__qty
        else:
            raise ValueError(f"Error: currency names are differ \'{self.__name}\' - \'{other.__name}\'")