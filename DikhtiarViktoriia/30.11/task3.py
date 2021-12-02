class Sum:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a} {self.b + other.b}"

a = Sum(3, 10)
b = Sum(4, 11)
print(a + b)