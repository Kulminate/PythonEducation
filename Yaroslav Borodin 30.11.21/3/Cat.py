from Animal import Animal


class Cat(Animal):
    title = "cat"

    def say(self) -> None:
        print("Мяу")

    def __add__(self, other) -> str:
        return title + "-" + other.title
