# Задание_1) Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на
# печать построчно последние строки в количестве lines. Написать несколько вызовов метода как для позитивных
# и негативных вариантов. Функция должна обрабатывать все ситуации


def read_last(lines, file_name):
    with open(file_name, "r") as file:
        return file.readlines()[-lines:]

num_lines = 2

try:
    file_name = input("Please enter file name to read:").strip()

    print(f"Last {num_lines} lines of file {file_name}:")

    lines = read_last(num_lines, file_name)

    for line in lines:
        print(line, end="")

except EOFError as err:
    print(err)
except IOError as err:
    print(err)
