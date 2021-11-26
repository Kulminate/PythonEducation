# 2) Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный,
# и False иначе.
def is_year_leap(year):
    if year in range (0,year+1,4):
        return True
    else: return False
print("Введите год: ")
print((is_year_leap(int(input()))))