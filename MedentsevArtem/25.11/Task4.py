def season(a):
    if 1 <= a <= 2 or a == 12:
        return 'зима'
    elif 3 <= a <= 5:
        return 'весна'
    elif 6 <= a <= 8:
        return 'лето'
    elif 9 <= a <= 11:
        return 'осень'
    else:
        return 'Перезапустите алгоритм и введите число от 1 до 12'





try:
    print(season(int(input('Введите номер месяца:'))))
except(ValueError, UnboundLocalError):
    print('Перезапустите алгоритм и введите число от 1 до 12')
