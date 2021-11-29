from Person import Person
person1 = Person("Михаил", "Козырев", "QA")
person1.display_info()

person2 = Person("Степан", "Иванов", "диджей")
person2.display_info()

person3 = Person("Леонид", "Смирнов", "разработчик")
person3.display_info()

del person2

input("Нажмите enter")