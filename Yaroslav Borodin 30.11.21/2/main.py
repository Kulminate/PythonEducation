# 2) Создайте класс Animal (животное) и разные производные от него подклассы:
# Fox, Bird, Cat, Dog и т.п. Реализуйте у них общий метод say(), который бы возвращал звук,
# издаваемый этим животным. Создайте кортеж из нескольких этих экземпляров классов,
# переберите их в цикле и выведите в консоль их звуки (вызовите метод say()).

from Pig import Pig
from Cat import Cat
from Dog import Dog

if __name__ == "__main__":
    animal_set = [Pig(), Cat(), Dog()]
    for animal in animal_set:
        animal.say()
