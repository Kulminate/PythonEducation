class Animal:
    title = "animal"

    def say(self) -> None:
        raise Exception("Don't implemented")

    def __add__(self, other):
        raise Exception("Don't implemented")
