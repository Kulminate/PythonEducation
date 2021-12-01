class Animal:

    color = 'black'

    def say(self):
        print('*Something on animal language*')


class Cat(Animal):

    def say(self):
        print('meow!')


class Dog(Animal):

    def say(self):
        print('Woof')


class Snake(Animal):

    def say(self):
        print('Ssss...')


class Chick(Animal):

    def say(self):
        print('Pi')


class Pigeon(Animal):

    def say(self):
        print('Coo-coo')