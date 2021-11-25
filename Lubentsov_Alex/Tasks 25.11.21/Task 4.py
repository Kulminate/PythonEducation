# 4) Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую
# время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(number_of_month):

        if number_of_month == 12 or 1 <= number_of_month <= 2:
            return"Winter"

        elif  3 <= number_of_month <= 5:
            return"Spring"

        elif 6 <= number_of_month <= 8:
            return"Summer"

        elif 9 <= number_of_month <= 11:
            return"Autumn"

        else:
            return "Incorrect number of month"

print(season(int(input())))
