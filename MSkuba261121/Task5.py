# 5) Написать метод century(), который возвращает век, в котором был этот год(века до н.е. тоже бывают)

year = int(input("Введите год"))


def century(year):
    if year % 100 == 0:
        a = year / 100
    else:
        a = int(year / 100) + 1

    return (str(a))
    if year % 100 == 0:
        a = year / -100
    else:
        a = int(year / -100) + 1


print(century(year))
