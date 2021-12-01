import datetime


class Date:
    def __init__(self, year, month, day):
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def checkDate(year, month, day):
        datetime.datetime(year, month, day)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, new_day):
        Date.checkDate(self.year, self.month, new_day)
        self.__day = new_day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, new_month):
        Date.checkDatetime(self.year, new_month, self.day)
        self.__month = new_month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        Date.checkDatetime(new_year, self.month, self.day)
        self.__year = new_year
