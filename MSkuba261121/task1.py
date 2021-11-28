# 1) Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить
# на печать построчно последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и негативных вариантов. Функция должна обрабатывать
# все ситуации

def read_last(lines, file):
    with open(file) as temp_file:
        scroll_lines = temp_file.readlines()# считываем строки из файла в список.
        strings = len(scroll_lines) # узнаем длину
        out_line = strings - lines # - кол-во

        if lines <= 0:
            print("Invalid number of lines")
        elif strings >= lines:
            print(f'last {lines} strings in file:')
            while out_line != strings:
                print(scroll_lines[out_line], end='')
                out_line += 1
        elif strings <= 0:
            print("empty file")

        else:
            print(f"В файле меньше {lines} строк")


file = "article.txt"
read_last(6, file)
read_last(1, file)
read_last(2, file)
read_last(-2, file)
read_last(4, file)
read_last(5, file)
