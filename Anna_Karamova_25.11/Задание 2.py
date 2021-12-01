#Задание 2: Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.

def is_year_leap(year):

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год является високосным")
        return True

    else:
        print("Год не является високосным")
        return False

year = int(input("Введите год для проверки:"))
is_year_leap(year)




