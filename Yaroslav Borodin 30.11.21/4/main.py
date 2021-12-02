from DateTime import DateTime

if __name__ == "__main__":
    dt = DateTime(2000, 12, 6, 15, 6, 15)

    print(DateTime.checkDateTime(1999, 12, 6, 41, 6, 41))  # Incorrect
    print(DateTime.checkDateTime(2013, 19, 6, 15, 6, 15))   # Incorrect
    print(DateTime.checkDateTime(2013, 12, 19, 15, 6, 15))  # Correct

    dt.nextSecond()
    dt.nextMinute()
    dt.nextHour()

    print(dt)
