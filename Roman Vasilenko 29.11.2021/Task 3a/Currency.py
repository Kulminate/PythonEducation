class Currency:

    def __init__(self, qty: float, name: str):
        self.qty = round(qty, 2)
        if name == 'rub':
            self.name = name
        elif name == '$':
            self.name = name
        elif name == 'uah':
            self.name = name
        else:
            raise ValueError('Value of name not valid. Must be "rub", "$", "uah"')




    @property
    def qty(self):
        return self.__qty

    @property
    def name(self):
        return self.__name

    @qty.setter
    def qty(self, qty):
        self.__qty = qty
    @name.setter
    def name(self, name):
        self.__name = name

    def print(self):
        print(f'{self.__qty} {self.__name}')

    def is_equal(self, currency):
        if self.__name == currency.__name and self.__qty == currency.__qty:
            return True
        else: return False

    def __str__(self):
        return f'{self.__qty} {self.__name}'

    def __add__(self, other):
        if self.__name == other.__name:
            return Currency(self.__qty + other.__qty, self.__name)
        else:
            raise Exception(f"Error:  currency names are differ '{self.__name}' - '{other.__name}'")

    def __sub__(self, other):
        if self.__name == other.__name:
            return Currency(self.__qty - other.__qty, self.__name)
        else:
            raise Exception(f"Error:  currency names are differ '{self.__name}' - '{other.__name}'")





