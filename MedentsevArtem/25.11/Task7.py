def multiplication_table():
    for i in range(1, 4):
        for j in range(1, 4):
            print(j, 'x', i, '=', j * i, end = '\t\t')
        print()


multiplication_table()
