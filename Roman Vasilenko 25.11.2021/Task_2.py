def is_year_leap(year: int = int(input('Enter year: '))):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False


print(is_year_leap())
