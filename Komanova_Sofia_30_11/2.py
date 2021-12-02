# 2) Создайте класс Animal (животное) и разные производные от него подклассы: Fox, Bird, Cat, Dog
# и т.п.
# Реализуйте у них общий метод say(), который бы возвращал звук, издаваемый этим животным. Создайте кортеж
# из нескольких этих экземпляров классов, переберите их в цикле и выведите в консоль их звуки
# (вызовите метод say()).

class Animal:
    def __init__(self, n:str, c:str):
        self.name = n
        self.colour = c



    def say(self):
        pass

class Fox(Animal):
    def __init__(self, n:str, c:str, l:int):
        super().__init__(n, c)
        self.legs = l

    def say(self):
        return "yippy"

class Bird(Animal):
    def __init__(self, n:str, c:str):
        super().__init__(n, c)

    def say(self):
        return "tweet"

class Cat(Fox):
    def __init__(self, n:str, c:str, l:int):
        super().__init__(n, c,l)

    def say(self):
        return "meaw"

class Dog(Fox):
    def __init__(self, n:str, c:str, l:int):
        super().__init__(n, c, l)

    def say(self):
        return "bark"


if __name__ == '__main__':
    cat1 = Cat("dfsf", "red", 4)
    dog1 =Dog("dsad", "black", 4)
    fox1 = Fox("sdadss", "red", 4)
    bird1 = Bird("ffsdf", "white")
    animals = {cat1, dog1, fox1, bird1}
    for i in animals:
        print(i.say())
