# Найти наибольший общий делитель двух чисел

def x(a, b):
    while b:
        a, b = b, a % b
    return a


print(x(int(input()), int(input())))
