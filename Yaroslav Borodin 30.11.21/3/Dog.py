from Animal import Animal


class Dog(Animal):
    title = "dog"

    def say(self) -> None:
        print("Гав")

    def __add__(self, other) -> str:
        return title + "-" + other.title
