# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month_number=input("Enter month number: ")):
    try:
        month_number = int(month_number)
        month_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
                      'autumn', 'autumn', 'autumn', 'winter']

        if 1 <= month_number <= 12:
            return month_list[month_number-1]

        else:
            return 'Incorrect month number!'
    except ValueError:
        print('Incorrect value')


print(season())
