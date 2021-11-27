# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines.
# Написать несколько вызовов метода как для позитивных и негативных вариантов. Функция должна обрабатывать все ситуации

def read_last(file: str = 'article.txt', lines: int = 0):
    try:
        with open(f'{file}', 'r', encoding="utf-8") as use_file:
            data_list = use_file.readlines()

        if 0 <= lines <= len(data_list):
            for i in range(1, lines+1):
                print(data_list[-i], end="")
        else:
            return print("Enter valid lines values. Must be between null and count lines of file")

    except FileNotFoundError as traceback:
        print(f"File not found. Traceback: {traceback}")



lines = int(input('Enter lines: '))
file = input('Enter file (try article.txt): ')
read_last(lines=lines, file=file)
