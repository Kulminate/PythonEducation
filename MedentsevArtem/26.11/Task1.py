# 1) Напишите функцию read_last(lines, file), которая будет
#    открывать определенный файл file и выводить на печать
#    построчно последние строки в количестве lines.
#    Написать несколько вызовов метода как для позитивных и негативных
#    вариантов. Функция должна обрабатывать все ситуации
def read_lines(lines, file):
    if lines < 0:
        raise ValueError
    d = {}
    lst = []
    cnt = 1
    with open(file, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            d.setdefault(cnt, i)
            cnt += 1
    if lines == len(d):
        for i in d:
            lst += [d[i]]
    else:
        cnt -= lines
        for i in range(lines):
            try:
                lst += [d[cnt]]
            except KeyError:
                return ['The number of lines should be equal or less than amount of lines in the article.txt.']
            cnt += 1
    return [line.rstrip() for line in lst]


try:
    print(*read_lines(int(input('Enter a number of lines:')), 'article.txt'), sep='\n')
except(ValueError, UnboundLocalError):
    print('Positive digits should be used.')