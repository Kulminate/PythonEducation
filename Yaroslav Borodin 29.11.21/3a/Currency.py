class Currency:

    def __init__(self, qty: float, name: str):
        self.qty = qty
        self.name = name

    def print(self):
        print(f"{self.qty:.2f} {self.name}")

    def isEqual(self, curr):
        if self.qty == curr.qty and self.name == curr.name:
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
        return self._qty

    @qty.setter
    def qty(self, qty):
        self._qty = qty
