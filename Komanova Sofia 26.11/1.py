# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и негативных вариантов.
# Функция должна обрабатывать все ситуации


def read_last(lines, file):
    with open(file) as new_file:
        list_of_lines = new_file.readlines()
        count_str = len(list_of_lines)
        out_line = count_str - lines
        if lines <=0:
            print("Неверное количество строк")
        elif count_str >= lines:
            print(f'Последние {lines} строки в файле:')
            while out_line != count_str:
                print(list_of_lines[out_line], end='')
                out_line+=1
        elif count_str <= 0:
            print("Файл пустой")
        else: print(f"В файле меньше {lines} строк")

#

file = "article.txt"
read_last(12, file)
read_last(-1, file)
read_last(3, file)
