class Metal:
    def __init__(self, weight: int):
        self.weight = weight

    def __add__(self, stick) -> int:
        return self.weight + stick.weight
