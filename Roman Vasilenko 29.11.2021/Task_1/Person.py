class Person:

    def __init__(self, name, surname, skill):
        self.name = name
        self.surname = surname
        self.skill = skill

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def skill(self):
        return self.__skill

    @name.setter
    def name(self, name):
        self.__name = name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @skill.setter
    def skill(self, skill):
        if skill == int(skill):
            self.__skill = skill
        else:
            raise Exception("Person skill does not excist")


    def info(self):
        return f'Person name is {self.__name}, surname is {self.__surname}, skill is {self.__skill}'

    def __del__(self):
        print(f'Good bye, mr {self.__name} {self.__surname}')
        del self

