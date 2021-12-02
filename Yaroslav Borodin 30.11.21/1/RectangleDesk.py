from Desk import Desk


class RectangleDesk(Desk):
    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b

    def calculate_area(self) -> float:
        return __a * __b
