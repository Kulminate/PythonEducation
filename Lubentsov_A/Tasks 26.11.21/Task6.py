# Создать файл, в котором есть несколько строк со временем формата ЧЧ: ММ: СС(т.е. 13:30:25)
# Каждая запись - это сколько времени нужно потратить на доставку одного подарка
#
# Если сумма всех времен, необходимых для доставки каждого подарка
# будет равна 24 часам то Санта сможет спасти рождество.
#
# Необходимо написать метод IsChristmasSave, в него необходимо
# передавать путь в файл со временем, далее вычитывать
# все время и сравнивать сумму с ожидаемой
import datetime


def IsChristmasSave(file):
    with open(file) as the_file:
        list_of_time = the_file.readlines()
        time = datetime.timedelta(days=0, hours=0)
        the_list = list()
        for i in list_of_time:
            x = i.replace('\n', '')
            the_list.append(x)
        for j in the_list:
            y = datetime.datetime.strptime(j, '%H:%M:%S')
            time2 = datetime.timedelta(hours=y.hour, minutes=y.minute, seconds=y.second)
            time += time2
        if time >= datetime.timedelta(days=1):
            print('Санта не сможет спасти рождество!')
        else:
            print('Санта сможет спасти рождество!')

the_file = "christmas.txt"
print(IsChristmasSave(the_file))