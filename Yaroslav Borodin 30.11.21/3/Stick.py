class Stick:
    def __init__(self, weight: int):
        self.weight = weight

    def __add__(self, metal) -> int:
        return self.weight + metal.weight
