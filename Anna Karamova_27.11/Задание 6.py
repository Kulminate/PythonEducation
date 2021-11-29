# 6) Создать файл, в котором есть несколько строк со временем формата ЧЧ: ММ: СС(т.е. 13:30:25)
# Каждая запись - это сколько времени нужно потратить на доставку одного подарка
# Если сумма всех времен, необходимых для доставки каждого подарка будет равна 24 часам, то Санта сможет спасти рождество.
# Необходимо написать метод IsChristmasSave, в него необходимо передавать путь в файл со временем,
# далее вычитывать все время и сравнивать сумму с ожидаемой


import datetime

file_name = "Для задания 6.txt"


def IsChristmasSave(file_name):
    with open(file_name, "r") as file:
        seconds = 0
        for line in file.readlines():
            date_string = datetime.datetime.strptime(line.strip(), "%H:%M:%S")
            current_time = date_string.time()
            seconds += current_time.second + current_time.minute * 60 + current_time.hour * 60 * 60
        return seconds <= 24 * 60 * 60


try:
    if IsChristmasSave(file_name):
        print("Санта может спасти Рождество")
    else:
        print("Санта не может спасти Рождество")
except Exception:
    print("Произошла ошибка")


