class Currency:

    def __init__(self, qty: float, name: str):
        self.__qty = qty
        self.__name = name

    def print(self):
        print(f"{self.__qty:.2f} {self.__name}")

    def isEqual(self, curr):
        if self.__qty == curr.qty and self.__name == curr.name:
            return True
        else:
            return False

    def __add__(self, other):
        if self.name == other.name:
            return self.qty+other.qty
        else:
            print(f"Error: currency names are differ '{self.name}' - '{other.name}'")

    def __sub__(self, other):
        if self.name == other.name:
            return self.qty - other.qty
        else:
            print(f"Error: currency names are differ '{self.name}' - '{other.name}'")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        self.__qty = qty
