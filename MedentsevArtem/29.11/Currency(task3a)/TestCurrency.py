from Currency import Currency

if __name__ == "__main__":
    cur1 = Currency(1, "грн")
    cur2 = Currency(10.11, "грн")
    cur1.print()
    print(cur1.isEqual(cur2))
    print(cur1 + cur2)
    print(cur1 - cur2)
