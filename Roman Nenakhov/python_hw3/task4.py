# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

seasons = ["Winter", "Spring", "Summer", "Autumn"]


def season(month):
    if 1 <= month <= 2 or month == 12:
        return seasons[0]
    elif 3 <= month <= 5:
        return seasons[1]
    elif 6 <= month <= 8:
        return seasons[2]
    elif 9 <= month <= 11:
        return seasons[3]
    else:
        return "Такого месяца не существует!!! Введите число от 1 до 12"


print(season(int(input())))
