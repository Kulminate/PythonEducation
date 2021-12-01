def century(y):
    try:
        year = int(y)
        cntr = 0
        if year > 0:
            if year % 100 == 0:
                cntr = year // 100
                print("{} век н.э.".format(cntr))
            else:
                cntr = (year // 100) + 1
                print("{} век н.э.".format(cntr))
        elif year < 0:
            if year % 100 == 0:
                cntr = year // -100
                print("{} век до н.э.".format(cntr))
            else:
                cntr = (year // -100) + 1
                print("{} век до н.э.".format(cntr))
        else:
            print("0 года не существует")
    except ValueError as e:
        print(e)


century(input("Введите год: "))