# 1) Напишите функцию read_last(lines, file),
# которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и негативных вариантов.
# Функция должна обрабатывать все ситуации

def read_last(lines, file):
    somefile = open(file, "r", encoding='utf8')
    file_lines = somefile.readlines()
    for line in range(lines):
        print(file_lines[-lines + line])
    somefile.close()


lines = int(input("Введите количество выводимых строк \n"))
file = "article.txt"
read_last(lines, file)