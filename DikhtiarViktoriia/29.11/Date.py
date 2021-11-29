import datetime

class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return (f"{self.__year}, {self.__month}, {self.__day}")

    @property
    def year(self):
        return self.__year

    @year.setter
    def set_year(self, y):
        self.__year = y

    @property
    def month(self):
        return self.__month

    @month.setter
    def set_month(self, m):
        self.__month = m

    @property
    def day(self):
        return self.__day

    @day.setter
    def set_day(self, d):
        self.__day = d

    def checkData(self, year: int, month: int, day: int):
        try:
            return datetime.date(year, month, day)
        except ValueError as e:
            print(e)

    def differenceIdDays(self, year: int, month: int, day: int):
        return (self.checkData(self.__year, self.__month, self.__day) - datetime.date(year, month, day)).days



d = Date(2012, 5, 23)
print(d.checkData(2012, 5, 23))
print(d.differenceIdDays(2012, 5, 10))


