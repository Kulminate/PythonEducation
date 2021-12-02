from Animal import Animal


class Pig(Animal):
    title = "pig"

    def say(self) -> None:
        print("Хрю")

    def __add__(self, other) -> str:
        return title + "-" + other.title
