class Currency:
    def __init__(self, qty: float, name: str):
        self.__qty = qty
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, new_qty):
        self.__qty = new_qty

    def __add__(self, other):
        if self.name != other.name:
            message = f"Error: currency names are different {self.__name} - {other.name}"
            raise ValueError(message)

        return Currency(self.qty + other.qty, self.name)

    def __sub__(self, other):
        if self.name != other.name:
            raise ValueError(f"Error: currency names are different {self.__name} - {other.name}")

        return Currency(self.qty - other.qty, self.name)

    def __eq__(self, other):
        return self.name == other.name and self.qty == other.qty

    def isEqual(self, other):
        return self == other

    def __str__(self):
        return "{amount:.2f}{name}".format(amount=self.qty, name=self.name)

    def print(self):
        print(self)

cur1 = Currency(4.0, "$")
cur2 = Currency(7.6, "$")
cur3 = cur1 + cur2

cur3.print()