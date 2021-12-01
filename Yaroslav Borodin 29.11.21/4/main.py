import datetime

from Date import Date

if __name__ == "__main__":
    date1 = Date(9, 12, 1999)
    print(Date.checkData(year=2000, day=15, month=5))
    print(date1.differenceIdDays(5, 6, 2001))
    print(datetime.timedelta(year=2005, month=2, day=19))

