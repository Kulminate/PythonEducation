# 5) Написать метод century(), который возвращает век, в котором был этот год(века до н.е. тоже бывают)
import math
def century(year):
    mod_year = abs(year)
    century = mod_year // 100 + (mod_year % 100 != 0)
    if year <0:
        print(f"{year}год - {century} век до н.э.")
    elif year==0:
        print("Нулевого года не существует")
    else: print(f"{year}год - {century} век н.э.")

century(2000)
century(0)
century(-2000)