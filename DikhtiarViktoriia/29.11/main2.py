from Currency import Currency

if __name__ == "__main__":
    currency1 = Currency(2.34, "руб")
    currency2 = Currency(3.56, "грн")
    currency1.print()
    print(currency1.isEqual(currency2))
    print(currency1.__add__(currency2))
    print(currency1.__sub__(currency2))