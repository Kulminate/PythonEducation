# 7) Вывести таблицу умножения в виде:
a = 0
for i in range(1, 10):
    print(end="\n")
    for x in range(1, 10):
        y = i * x
        print('{} * {} = {}'.format(x, i, y), end="\t")