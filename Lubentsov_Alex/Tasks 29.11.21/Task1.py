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

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


    def __del__(self):
        if self.gender == 'мужчина':
            text = "мистер "
        else:
            text = "миссис "
        print(f"До свидания " + text, self.name, self.surname)

    def info(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Пол: {self.gender}"

if __name__ == '__main__':
    Person1 = Person("Сергей", "Петров", "мужчина")
    Person2 = Person("Алена", "Баринова", "женщина")
    Person3 = Person("Василий", "Васильев", "мужчина")

    print(Person1.info())
    print(Person2.info())
    print(Person3.info())
    del (Person2)
    input()


