# Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file и выводить
# на печать построчно последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и
# негативных вариантов. Функция должна обрабатывать все ситуации


def read_last(lines, my_file):
    with open(my_file) as new_file:
        list_of_strings = new_file.readlines()
        count_strings = len(list_of_strings)
        out_line = count_strings - lines
        if lines <= 0:
            print("Неверное количество строк")
        elif count_strings >= lines:
            print(f'Последние {lines} строки в файле:')
            while out_line != count_strings:
                print(list_of_strings[out_line], end='')
                out_line += 1
        elif count_strings <= 0:
            print("Файл пустой")
        else:
            print(f"В файле меньше {lines} строк")


my_file = "article.txt"
read_last(int(input("Сколько последних строк показать? ")), my_file)

