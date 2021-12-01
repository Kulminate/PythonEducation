from Animal import *

cat = Cat()
dog = Dog()
snake = Snake()
chick = Chick()
pigeon = Pigeon()

animal_tuple = cat, dog, snake, chick, pigeon

for animal in animal_tuple:
    animal.say()
