# 1)  У класса Person есть метод, который возвращает строку,
# включающую в себя всю информацию о сотруднике.
# Класс Person содержит деструктор, который выводит на экран
# фразу "До свидания, мистер …" (вместо троеточия должны
# выводиться имя и фамилия объекта).
# В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.
# В конце программы добавьте функцию input(), чтобы скрипт не завершился
# сам, пока не будет нажат Enter. Иначе вы сразу увидите как удаляются
# все объекты при завершении работы программы.
# В Python деструктор используется редко, так как интерпретатор и без
# него хорошо убирает "мусор".

class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        try:
            return f'Привет, я {self.sex}, меня зовут {self.name}, мне {self.age} лет.'
        except AttributeError:
            raise ValueError("Invalid data.")

    def __del__(self) -> None:
        try:
            if self.sex == 'мужчина':
                print(f'До свидания, мистер {self.name}.')
            else:
                print(f'До свидания, миссис {self.name}.')
        except AttributeError:
            raise ValueError("Invalid data.")

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, s) -> None:
        if s.lower() == 'м' or s.lower() == 'мужской' or s.lower() == 'мужчина':
            self.__sex = 'мужчина'
        elif s.lower() == 'ж' or s.lower() == 'женский' or s.lower() == 'женщина':
            self.__sex = 'женщина'
        else:
            raise ValueError("Invalid data")

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, a) -> None:
        if a.isdigit():
            if 16 <= int(a) <= 65:
                self.__age = a
            else:
                raise ValueError("Age should be between 16 and 65.")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, n) -> None:
        if n.isalpha():
            self.__name = n
        else:
            raise ValueError
