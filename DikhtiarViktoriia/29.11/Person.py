class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def inf(self):
        print(self.name, self.surname)

    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}")