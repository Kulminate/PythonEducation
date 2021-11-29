from random import randrange


class SomeNumber:
    n = 0

    def __init__(self, n):
        self.n = n

    @property
    def n(self):
        return self.__firstname

    @firstname.setter
    def n(self, n):
        if n.isdigit():
            self.__n = int(n)
        else:
            raise ValueError

    def print(self):
        print(f'Число: {self.__n}')

    def isBooleen(self):
        return f'firstname: {self.__firstname}, surname: {self.__lastname}'

    def __del__(self):
        print(f'Досвидания, мистер {self.__firstname} {self.__lastname} \n(efficiency: {self.efficiency})')
