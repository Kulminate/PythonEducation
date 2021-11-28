# Создать файл, в котором есть несколько строк со временем формата ЧЧ: ММ: СС(т.е. 13:30:25)
# Каждая запись - это сколько времени нужно потратить на доставку одного подарка
#
# Если сумма всех времен, необходимых для доставки каждого подарка
# будет равна 24 часам то Санта сможет спасти рождество.
#
# Необходимо написать метод IsChristmasSave, в него необходимо
# передавать путь в файл со временем, далее вычитывать
# все время и сравнивать сумму с ожидаемой
from datetime import timedelta, datetime


def IsChristmasSave(file):
    with open(file) as new_file:
        list_of_strings = new_file.readlines()
        all_time = timedelta(days=0, hours=0)
        new_list = list()
        for i in list_of_strings:
            x = i.replace('\n', '')
            new_list.append(x)
        for j in new_list:
            y = datetime.strptime(j, '%H:%M:%S')
            new_all_time = timedelta(hours=y.hour, minutes=y.minute, seconds=y.second)
            all_time += new_all_time
        if all_time >= timedelta(days=1):
            return 'Рождество не спасено :( '
        else:
            return 'Рождество спасено! :) '


my_file = "christmas_time.txt"
print(IsChristmasSave(my_file))
