from Currency import Currency

if __name__ == '__main__':

    rub_1 = Currency(150.55, 'rub')
    rub_2 = Currency(120.55, 'rub')
    dollar = Currency(25.555, '$')
    euro = Currency(50.555555, 'uah')

    rub_1.print()
    dollar.print()
    euro.print()

    print(rub_1.is_equal(rub_2))
    print(rub_1.is_equal(dollar))

    money_sum = rub_1 + rub_2
    print(money_sum)
    # print(rub_1 + dollar)

    print(rub_1 - rub_2)
    # print(rub_1 - dollar)


