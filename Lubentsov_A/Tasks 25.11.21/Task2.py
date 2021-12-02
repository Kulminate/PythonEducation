#  2) Написать функцию is_year_leap, принимающую 1 аргумент — год,
#  и возвращающую True,  если год високосный, и False иначе.


#   y=1900
def is_year_leap(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False

print(is_year_leap(int(input())))