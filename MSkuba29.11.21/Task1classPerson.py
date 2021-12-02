class Person:

    def __init__(self, name, skill ):
        self.name = name

        self.skill = skill

    def __del__(self):
        print(f"Good bye Mr {self.name} ")

    def inform(self):
        return f"Worker {self.name}, Skill: {self.skill}"