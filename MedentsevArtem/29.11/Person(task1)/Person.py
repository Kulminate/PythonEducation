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

    def __str__(self):
        return f'Привет, я {self.sex}, меня зовут {self.name}, мне {self.age} лет.'

    def __del__(self):
        if self.sex == 'мужчина':
            print(f'До свидания, мистер {self.name}.')
        else:
            print(f'До свидания, миссис {self.name}.')

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, s):
        if s.lower() == 'м' or s.lower() == 'мужской' or s.lower() == 'мужчина':
            self.__sex = 'мужчина'
        elif s.lower() == 'ж' or s.lower() == 'женский' or s.lower() == 'женщина':
            self.__sex = 'женщина'
        else:
            raise ValueError

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        if a.isdigit():
            if 16 <= int(a) <= 65:
                self.__age = a
            else:
                raise ValueError
