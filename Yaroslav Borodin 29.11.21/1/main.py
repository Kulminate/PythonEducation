from typing import List

from Person import Person


def fire_person(persons: List[Person]) -> None :
    min_eff = persons[0].efficiency
    min_index = 0
    for i in range(1, len(persons)):
        if persons[i].efficiency <= min_eff:
            min_eff = persons[i].efficiency
            min_index = i
    del persons[min_index]


if __name__ == "__main__":
    Persons = [Person("Mark", "Paul"), Person("Fifty", "Cent"), Person("Alister", "Crawley")]
    fire_person(Persons)
    end = input()
