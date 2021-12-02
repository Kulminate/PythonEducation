# 7) Вывести таблицу умножения в виде:
# 1 x 1 = 1		2 x 1 = 2 	3 x 1 = 3
# 1 x 2 = 2		2 x 2 = 4		3 x 2 = 6
# 1 x 3 = 3		2 x 3 = 6		3 x 3 = 9


for table in range(1, 4):
    for line in range(1, 4):
        result = eval('{} * {}'.format(line, table))
        print('{} x {} = {}'.format(line, table, result), end='\t')
    print(end='\n')

