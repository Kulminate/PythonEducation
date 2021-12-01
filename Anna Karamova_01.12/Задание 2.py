# Создайте класс Animal (животное) и разные производные от него подклассы: Fox, Bird, Cat, Dog и т.п.
# Реализуйте у них общий метод say(), который бы возвращал звук, издаваемый этим животным.
# Создайте кортеж из нескольких этих экземпляров классов, переберите их в цикле и выведите в консоль их звуки (вызовите метод say()).

class Animal(object):
    def say(self):
        raise Exception ("This method must be overridden")


class Dog(Animal):
    def say(self):
        print("woof")

    def __str__(self):
        return "Dog"


class Cat(Animal):
    def say(self):
        print("meow")

    def __str__(self):
        return "Cat"


class Bird(Animal):
    def say(self):
        print("tweet")

    def __str__(self):
        return "Bird"


class Cow(Animal):
    def say(self):
        print("moo")

    def __str__(self):
        return "Cow"


animals = (Dog(), Cat(), Bird(), Cow())

for animal in animals:
    print(f"What does the {animal} say?")
    animal.say()
