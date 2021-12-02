from Task4_Class_Date import Date
if __name__ == '__main__':

    date1 = Date(27,8,2011)
    print(date1.month)
    date1.day= 40
    print(date1.day)
    date1.month = 11
    date1.year = 2013
    print(date1.day, date1.month, date1.year)
    print(Date.checkData(10, 3, 2010))
    date1.differenceIdDays(6,6,2013)