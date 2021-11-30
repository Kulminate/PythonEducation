#  У класса Person есть метод, который возвращает строку,
#  включающую в себя всю информацию о сотруднике.
#
# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
# (вместо троеточия должны выводиться имя и фамилия объекта).
#
# В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.
# В конце программы добавьте функцию input(), чтобы скрипт не завершился сам,
# пока не будет нажат Enter. Иначе вы сразу увидите
# как удаляются все объекты при завершении работы программы.
# В Python деструктор используется редко,
# так как интерпретатор и без него хорошо убирает "мусор".

class Person:
    name = str()
    surname = str()
    qualify = int()
    sex = str()

    def __init__(self, name, surname, sex, qualify=1):
        self.name = name
        self.surname = surname
        self.qualify = qualify
        self.sex = sex

    def show_info(self):
        show = [self.name, self.surname, self.sex, str(self.qualify)]
        return str(' '.join(show))

    def __del__(self):
        ls = [self.name, self.surname]
        if self.sex == 'мужчина':
            text = "мистер "
        else:
            text = "миссис "

        print('До свидания, ' + text + str(' '.join(ls)))


if __name__ == '__main__':
    person1 = Person("Иван", "Иванов", "мужчина", 100)
    person2 = Person("Петр", "Петров", "мужчина", 88)
    person3 = Person("Елена", "Головач", "женщина", 57)

    print(person1.show_info())
    print(person2.show_info())
    print(person3.show_info())
    del person3
    input('')
