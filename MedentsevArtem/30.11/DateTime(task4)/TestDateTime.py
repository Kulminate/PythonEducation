from DateTime import DateTime


if __name__ == "__main__":
    a = DateTime(2200, 12, 31, 23, 59, 59)
    a.nextSecond()
    print(a)