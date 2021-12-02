class Animal:
    def say(self):
        raise Exception

    def __str__(self):
        return self.say()

class Dog(Animal):
    def say(self):
        return "Woof-Woof"

class Donkey(Animal):
    def say(self):
        return "Hee-Haw"

class Mouse(Animal):
    def say(self):
        return "squeak-squeak"

animal_tuple = (Dog(), Donkey(), Mouse())

for i in animal_tuple:
    print(i.say())