# Написать метод century(), который возвращает век, в котором был этот год(века до н.е. тоже бывают)

def century(year):
    try:

        year = int(year)

        if year >= 0:

            if year > 2021:
                print('The year has not come yet')

            elif year % 100 == 0:
                print(f'It\'s {year // 100}st century!!')
            elif year == 0:
                print(f'Do not enter ZERO!!!!!!!!!!!!!!')
            else:
                print(f'It\'s {(year // 100)+1}st century!!')
        elif year <0:
            print(f'It\'s {-(year // 100)}st BC!!')

    except ValueError as trace:
        print(f'ValueError. Enter valid year.  Traceback: {trace}')


year = input('Enter year: ')
century(year)

