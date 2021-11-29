from Person import Person

if __name__ == "__main__":
    skill_list = []
    tom = Person('Tom', 'Holand', 15)
    skill_list.append(tom)
    toby = Person('Toby', 'Maguire', 15)
    skill_list.append(toby)
    andrew = Person('Andrew', 'Garfield', 15)
    skill_list.append(andrew)

    print(tom.info())
    print(toby.info())
    print(andrew.info())

    for person in skill_list:
        if person.skill == min(tom.skill, toby.skill, andrew.skill):
            print(f'{person.name} worse than other. His skill is {person.skill}')
            person.__del__()

    input()



