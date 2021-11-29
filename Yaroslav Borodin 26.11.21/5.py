# 5) Написать метод century(), который возвращает век,
# в котором был этот год(века до н.е. тоже бывают)
import math


def century(era, year):
    century = math.ceil(int(year) / 100)
    res = str(century) + " век"
    if era == "0":
        res += " до н.э."
    else:
        res += " н.э."
    return res


correct_input = False
while not correct_input:
    input_era = input("Выберите хронологический период \n(0 - до н.э., 1 - н.э.)\n")
    if input_era not in ("0", "1"):
        print("Некорректный ввод эры, повторите ввод")
        continue
    input_year = input("Введите год (целое число начиная с 1) \n(например: 2015, 3, 564)\n")
    if not input_year.isdigit() or input_year == "0":
        print("Некорректный ввод года, повторите ввод\n")
        continue
    correct_input = True

print(century(input_era, input_year))
