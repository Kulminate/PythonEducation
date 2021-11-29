# Создать файл, в котором есть несколько строк со временем формата ЧЧ: ММ: СС(т.е. 13:30:25)
# Каждая запись - это сколько времени нужно потратить на доставку одного подарка
# Если сумма всех времен, необходимых для доставки каждого подарка будет равна 24 часам то Санта сможет спасти рождество
# Необходимо написать метод IsChristmasSave, в него необходимо передавать путь в файл со временем,
# далее вычитывать все время и сравнивать сумму с ожидаемой


from datetime import time


def isChristmasSave(path_file):
    try:
        hours = int()
        minutes = int()
        seconds = int()

        with open(path_file, "r", encoding= 'utf-8') as file:
            time_list = file.readlines()

        for index in range(len(time_list)-1):
            time_list[index] = time_list[index][:-1]

        for index in range(len(time_list)):

            hours += int(time_list[index][0:2])
            minutes += int(time_list[index][3:5])
            seconds += int(time_list[index][6:8])

        hours += minutes // 60
        minutes %= 60
        minutes += seconds // 60
        seconds %= 60

        print(f'List of times in entered file:  {time_list}')
        print(f'The time Santa spent delivering gifts: {time(hours, minutes, seconds)} \n Christmas is saved!!! ')

    except ValueError as trace:
        print(f'Santa lose Christmas!! Not enough time :( \n Traceback: {trace}')
    except FileNotFoundError:
        print('File not found!')


path = input('Enter path to file or name of file (try time.txt): ')
isChristmasSave(path)
