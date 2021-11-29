from Task1classPerson import Person

if __name__ == '__main__':
    b = Person("Benny",  8)
    s = Person("Shtak",  4)
    k = Person("Korney", 1)

    print(b.inform())
    print(s.inform())
    print(k.inform())
    del (k)
    input()