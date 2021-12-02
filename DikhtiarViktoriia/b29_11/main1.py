from Person import Person

if __name__ == "__main__":
    person1 = Person("Иван", "Иванов")
    person2 = Person("Петр", "Петров")
    person3 = Person("Сергей", "Сергеев")
    person1.__del__()
    person2.__del__()
    person3.__del__()

input()