class Overload:
    def __init__(self, a):
        self.a = a

    def __add__(self, other, other2=None):
        if other2 != None:
            try:
                return f"{self.a + other.a + other2.a}"
            except(ValueError, UnboundLocalError, TypeError):
                raise ValueError("The given data is wrong.")
        else:
            try:
                return f"{self.a + other.a}"
            except(ValueError, UnboundLocalError, TypeError):
                raise ValueError("The given data is wrong.")
