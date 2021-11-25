def season(m):
    if m >= 1 and m < 3 or m == 12:
        return "зима"
    elif m > 2 and m < 6:
        return "весна"
    elif m > 5 and m < 9:
        return "лето"
    elif m > 8 and m < 12:
        return "осень"
    else:
        return "Некорректное число"

print(season(int(input("Введите номер месяца: "))))