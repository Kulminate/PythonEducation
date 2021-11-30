import datetime


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def checkData(day=9, month=12, year=1999):
        try:
            datetime.date(year, month, day)
        except ValueError:
            print("Некорректная дата")
            return False
        else:
            return True

    def differenceIdDays(self, day: int, month: int, year: int):
        self_td = datetime.timedelta(self._year, self._month, self._day)
        other_td = datetime.timedelta(year, month, day)
        return (self_td-other_td).days

    @property
    def day(self):
        return self._day

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @day.setter
    def day(self, day):
        if Date.checkData(day=day):
            self._day = day
        else:
            raise ValueError

    @year.setter
    def year(self, year):
        if Date.checkData(year=year):
            self._year = year
        else:
            raise ValueError

    @month.setter
    def month(self, month):
        if Date.checkData(month=month):
            self._month = month
        else:
            raise ValueError
