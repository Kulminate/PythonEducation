# 5) Написать метод century(), который возвращает век,
#    в котором был этот год(века до н.е. тоже бывают)
def century(year):
    if len(year) > 2:
        year = int(year)
        if year >= 0:
            result = {'cent': int(year) // 100 + 1, 'era': 'A.D.'}
        else:
            result = {'cent': int(year) // -100 + 1, 'era': 'B.C.'}
    else:
        year = int(year)
        if year >= 0:
            result = {'cent': int(year) // 100 + 1, 'era': 'A.D.'}
        else:
            result = {'cent': int(year) // -100 + 1, 'era': 'B.C.'}

    return "{r[cent]} {r[era]}".format(r=result)


try:
    print(century(input('Enter a year:')))
except ValueError:
    print('Use digits as input please.')
