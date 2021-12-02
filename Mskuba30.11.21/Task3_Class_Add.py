class Add:
    def __init__(self, a:int, b:str):
        self.__a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @ a.setter
    def a(self, a):
        self.__a = a

    def __add__(self, other):
        return f"{self.__a + other.__a} {self.b + other.b}"

if __name__ == '__main__':
    num1 = Add(3,'qwerty')
    num2 = Add(4,'asdfg')
    print(num1+num2)