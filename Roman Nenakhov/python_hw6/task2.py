# Создайте класс Animal(животное) и разные производные от
# него подклассы: Fox, Bird, Cat, Dog и т.п.Реализуйте у них общий
# метод say(), который бы возвращал звук, издаваемый этим животным.Создайте
# кортеж из нескольких этих экземпляров классов, переберите их в цикле и
# выведите в консоль их звуки(вызовите метод say()).


class Animal:

    def say(self):
        print('speaks in his language')


class Dog(Animal):

    def say(self):
        print('Woof!!!!')


class Cat(Animal):

    def say(self):
        print('Meow!!!!')


class Frog(Animal):

    def say(self):
        print('Croak!!!')


class Cow(Animal):

    def say(self):
        print('Moooooooo!!!')


class Fly(Animal):

    def say(self):
        print('Bzzzzzzzzz')


dog = Dog()
cat = Cat()
frog = Frog()
cow = Cow()
fly = Fly()

animals = dog, cat, frog, cow, fly

for animal in animals:
    animal.say()