from datetime import DateTime

if __name__ == '__main__':

    datetime_1 = DateTime(10, 10, 2021, 5, 45, 55)

    print(DateTime.check_time(23, 59, 59))
    print(DateTime.check_time(0, 0, 0))
    # DateTime.check_time(555, 222, 333)
    # DateTime(11, 11, 2021, 55, 567, 231)

    # method __str__
    print(datetime_1)

    print(DateTime.check_datetime(10, 10, 2021, 5, 45, 55))
    print(DateTime.check_datetime(555, 222, 333, 55, 567, 231))

    # Changing dateTime

    chg_date = DateTime(31, 12, 1999, 23, 59, 59)
    print(chg_date)
    chg_date.next_second()
    print(chg_date)
    chg_date.next_minute()
    print(chg_date)
    chg_date.next_hour()
    print(chg_date)




