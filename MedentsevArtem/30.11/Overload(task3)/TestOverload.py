from Overload import Overload
def try_to_overload():
    a = Overload(2)
    b = Overload(3)
    c = Overload(4)
    print(a.__add__(b, c))


try_to_overload()
