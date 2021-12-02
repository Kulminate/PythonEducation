# Написать метод century(), который возвращает век,
# в котором был этот год(века до н.е. тоже бывают)



def century(year):
    the_year = abs(year)
    the_century = the_year // 100 + (the_year % 100 != 0)
    if year < 0:
        print(f"{year}год - {the_century} век до н.э.")
    elif year == 0:
        print("Нулевого года не существует")
    else:
        print(f"{year}год - {the_century} век н.э.")


century(2030)
century(0)
century(-700)