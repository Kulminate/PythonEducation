from Currency import Currency

if __name__ == "__main__":
    cur1 = Currency(10.11, "$")
    cur2 = Currency(10.11, "грн")
    cur1.print()
    print(cur1.isEqual(cur2))
    print(cur1.__add__(cur2))
    print(cur1.__sub__(cur2))