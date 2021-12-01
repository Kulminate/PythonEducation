from random import randrange


class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.efficiency = randrange(1, 15)

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str) -> None:
        if firstname.isalpha():
            self.__firstname = firstname
        else:
            raise ValueError

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str) -> None:
        if lastname.isalpha():
            self.__lastname = lastname
        else:
            raise ValueError

    def __str__(self) -> str:
        return f'firstname: {self.__firstname}, surname: {self.__lastname}'

    def __del__(self) -> None:
        print(f'Досвидания, мистер {self.__firstname} {self.__lastname} \n(efficiency: {self.efficiency})')
