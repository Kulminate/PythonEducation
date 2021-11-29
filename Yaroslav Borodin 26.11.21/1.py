# 1) Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и негативных вариантов.
# Функция должна обрабатывать все ситуации

def read_last(lines, file):
    some_file = open(file, "r", encoding='utf8')
    file_lines = some_file.readlines()
    if lines < 0:
        ln_range = abs(lines)
    else:
        ln_range = lines
    for line in range(1, ln_range + 1):
        if lines > 0:
            print(file_lines[-lines + line - 1].replace("\n", ''))
        else:
            print(file_lines[line - 1].replace("\n", ''))
    some_file.close()


# lines = int(input("Введите количество выводимых строк \n"))
file = "article.txt"
# read_last(lines, file)


read_last(3, file)
print()
read_last(2, file)
print()
read_last(-3, file)
print()
read_last(-2, file)
print()
read_last(0, file)
