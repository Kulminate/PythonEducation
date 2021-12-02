class Animal:
    def say(self):
        raise Exception ("Метод должен быть переопределен у наследника")

    def __str__(self):
        return self.say()

class Fox(Animal):
    def say(self):
        return "yow-wow-wow"

class Cat(Animal):
    def say(self):
        return "meow-meow"

class Dog(Animal):
    def say(self):
        return "woof-woof"

animal_tuple = (Fox(), Cat(), Dog())

for i in animal_tuple:
    print(i.say())