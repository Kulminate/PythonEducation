class Currency:

    def __init__(self, qty: float, name: str) -> None:
        self.__qty = qty
        self.__name = name

    def print(self) -> None:
        print(f"{self.__qty:.2f} {self.__name}")

    def isEqual(self, curr) -> bool:
        if self.__qty == curr.qty and self.__name == curr.name:
            return True
        else:
            return False

    def __add__(self, other) -> int:
        if self.name == other.name:
            return self.qty + other.qty
        else:
            print(f"Error: currency names are differ '{self.name}' - '{other.name}'")

    def __sub__(self, other) -> float:
        if self.name == other.name:
            return self.qty - other.qty
        else:
            print(f"Error: currency names are differ '{self.name}' - '{other.name}'")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError

    @property
    def qty(self) -> float:
        return self.__qty

    @qty.setter
    def qty(self, qty: float) -> None:
        self.__qty = qty
