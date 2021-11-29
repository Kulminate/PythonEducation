from random import randrange


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.efficiency = randrange(1, 15)

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        if firstname.isalpha():
            self.__firstname = firstname
        else:
            raise ValueError

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        if lastname.isalpha():
            self.__lastname = lastname
        else:
            raise ValueError

    def __str__(self):
        return f'firstname: {self.__firstname}, surname: {self.__lastname}'

    def __del__(self):
        print(f'Досвидания, мистер {self.__firstname} {self.__lastname} \n(efficiency: {self.efficiency})')
