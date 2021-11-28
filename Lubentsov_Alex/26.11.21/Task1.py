# 1) Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить
# на печать построчно последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и негативных вариантов.
# Функция должна обрабатывать все ситуации


# article.txt:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(file: str = 'article.txt', lines: int = 2):
    try:
        with open(f'{file}', 'r', encoding="utf-8") as the_file:
            the_list = the_file.readlines()

        if 0 <= lines <= len(the_list):
            for i in range(1, lines+1):
                print(the_list[-i], end="\n")
        else:
            print("Неверное колличество строк")

    except FileNotFoundError as traceback:
        print(f"File not found. Traceback: {traceback}")

lines = int(input('Введите колличество строк: '))
file = input('Введите путь к файлу article.txt: ')
read_last(lines=lines, file=file)