# Задание 5) Написать метод century(), который возвращает век, в котором был этот год(века до н.е. тоже бывают)
import math


def get_century(year):
    if year > 0:
        century = year // 100 + 1
    else:
        century = (int(math.fabs(year)) // 100 + 1) * -1
    return century


year = int(input("Введите год для проверки:"))
century = get_century(year)
print(f"Это {int(math.fabs(century))}", "век", "до нашей эры" if century < 0 else "")
