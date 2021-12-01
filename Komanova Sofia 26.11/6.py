# 6) Создать файл, в котором есть несколько строк со временем формата ЧЧ: ММ: СС(т.е. 13:30:25)
# Каждая запись - это сколько времени нужно потратить на доставку одного подарка
#
# Если сумма всех времен, необходимых для доставки каждого подарка будет равна 24 часам то Санта
# сможет спасти рождество.
#
# Необходимо написать метод IsChristmasSave, в него необходимо передавать путь в файл со временем,
# далее вычитывать все время и сравнивать сумму с ожидаемой
from datetime import timedelta, datetime


def IsChristmasSave(file):
    with open(file) as new_file:
        list_of_lines = new_file.readlines()
        all_time = timedelta(days= 0,hours=0)
        new_list = list()
        for i in list_of_lines:
            a = i.replace('\n', '')
            new_list.append(a)
        for n in new_list:
              s = datetime.strptime(n,'%H:%M:%S')
              td2 = timedelta(hours=s.hour, minutes=s.minute, seconds=s.second)
              all_time+=td2
        if (all_time >= timedelta(days=1)):
             return 'Санта не сможет спасти рождество'
        else: return 'Санта сможет спасти рождество'




file1 = "time.txt"
file2 = "timeFalse.txt"
print(IsChristmasSave(file1))
print(IsChristmasSave(file2))

