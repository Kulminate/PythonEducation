# 7) Вывести таблицу умножения в виде:
# 1 x 1 = 1		2 x 1 = 2 	    3 x 1 = 3
# 1 x 2 = 2		2 x 2 = 4		3 x 2 = 6
# 1 x 3 = 3		2 x 3 = 6		3 x 3 = 9

def mult_tbl(num):
  for i in range(1, num+1):
      for j in range(1, num+1):
         print(j, "x", i, '=', i*j , end='   ')
      print("\t")

mult_tbl(3)