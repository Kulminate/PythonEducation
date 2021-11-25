def is_year_leap(year):
        if year % 100 != 0 and year % 4 == 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False


try:
    print(is_year_leap(int(input('Enter a year:'))))
except(ValueError, UnboundLocalError):
    print('Digits should be used.')