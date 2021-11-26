# 7) Вывести таблицу умножения в виде:
# 1 x 1 = 1		2 x 1 = 2 	    3 x 1 = 3
# 1 x 2 = 2		2 x 2 = 4		3 x 2 = 6
# 1 x 3 = 3		2 x 3 = 6		3 x 3 = 9

column = 1
number_of_columns = 3
for i in range(1, 10):
    for k in range(1, 10):
        print(f"{i} x {k} = {i * k}\t\t", end="")
        if column % 3 == 0:
            print()
            column = 1
        else:
            column += 1
