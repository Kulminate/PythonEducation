# Написать метод century(), который возвращает век,
# в котором был этот год(века до н.е. тоже бывают)
import math


def century(year):
    my_year = abs(year)
    my_century = my_year // 100 + (my_year % 100 != 0)
    if year < 0:
        print(f"{year}год - {my_century} век до н.э.")
    elif year == 0:
        print("Нулевого года не существует")
    else:
        print(f"{year}год - {my_century} век н.э.")


century(2021)
century(0)
century(-400)
