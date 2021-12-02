from Desk import Desk
from math import pi


class RoundDesk(Desk):
    def __init__(self, r: float):
        self.__r = r

    def calculate_area(self) -> float:
        return pi * self.__r ** 2
