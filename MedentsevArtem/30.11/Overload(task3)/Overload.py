class Overload:
    def __init__(self, a):
        self.a = a

    def __add__(self, other, other2=None):
        if other2 != None:
            return f"{self.a + other.a + other2.a}"
        else:
            return f"{self.a + other.a}"
