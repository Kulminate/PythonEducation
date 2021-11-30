# 6) Создать файл, в котором есть несколько строк
#    со временем формата ЧЧ: ММ: СС(т.е. 13:30:25)
#    Каждая запись - это сколько времени нужно потратить
#    на доставку одного подарка
#    Если сумма всех времен, необходимых для доставки каждого
#    подарка будет равна 24 часам то Санта сможет спасти рождество.
#    Необходимо написать метод IsChristmasSave, в него необходимо
#    передавать путь в файл со временем, далее вычитывать все время
#    и сравнивать сумму с ожидаемой
from datetime import datetime, timedelta
def IsChristmasSave(file):
    tm = timedelta()
    with open(file, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            h, m, s = i.rstrip().split(':')
            tm += timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    if tm == timedelta(hours=24):
        return 'Санта сможет спасти рождество. :,)'
    else:
        return 'Санта не сможет спасти рождество. :\'('


# позитивный исход в файле "для_счастливого_Рождества.txt"
# негативный исход в файле "delivery_time.txt"
try:
    print(IsChristmasSave('для_счастливого_Рождества.txt'))
except ValueError:
    print('Неверный формат данных.')