def is_year_leap(y):
    if y % 100 == 0 and y % 400 == 0:
        return True
    if y % 4 == 0 and not y % 100 == 0:
        return True


year = int(input("Ведите год\n"))
if is_year_leap(year):
    print("Это високосный год")
else:
    print("Это не високосный год")
