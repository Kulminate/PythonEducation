# Задание 4) Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
#и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень)

def season(month_number: int) -> str:

    if month_number == 1 or month_number == 2 or month_number == 12:
        return "зима"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "весна"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "лето"
    elif month_number == 8 or month_number == 9 or month_number == 10:
        return "осень"

    return "ошибка"


month_number = int(input("Введите номер месяцa для проверки:"))
print("Это", season(month_number))

