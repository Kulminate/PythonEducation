# 6) Создать файл, в котором есть несколько строк со временем формата ЧЧ:ММ:СС(т.е. 13:30:25)
# Каждая запись - это сколько времени нужно потратить на доставку одного подарка
# Если сумма всех времен, необходимых для доставки каждого
# подарка будет равна 24 часам то Санта сможет спасти рождество.
# Необходимо написать метод IsChristmasSave,
# в него необходимо передавать путь в файл со временем, далее вычитывать
# все время и сравнивать сумму с ожидаемой
import datetime, time


def IsChristmasSave(path):
    required_time = datetime.timedelta()
    deadline = datetime.timedelta(hours=24)
    with open(path, "r", encoding="utf8") as file:
        for time_line in file:
            t = time.strptime(time_line.replace('\n', ''), "%H:%M:%S")
            required_time += datetime.timedelta(hours=t.tm_hour, minutes=t.tm_min, seconds=t.tm_sec)
    if required_time <= deadline:
        return True
    else:
        return False


default_path = "file.txt"
print(IsChristmasSave(default_path))
