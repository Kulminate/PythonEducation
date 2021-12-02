import datetime


class Date:

    def __init__(self, year: int, month: int, day: int) -> None:
        self.__year = year
        self.__month = month
        self.__day = day

    @staticmethod
    def checkData(year=2000, month=6, day=15) -> bool:
        try:
            datetime.date(year, month, day)
        except ValueError:
            return False
        else:
            return True

    def differenceIdDays(self, year: int, month: int, day: int) -> int:
        self_td = datetime.timedelta(self.__day + self.__year * 365 + self.__month * 31)
        other_td = datetime.timedelta(day + year * 365 + month * 31)
        return abs((self_td - other_td).days)

    @property
    def day(self) -> int:
        return self.__day

    @property
    def year(self) -> int:
        return self.__year

    @property
    def month(self) -> int:
        return self.__month

    @day.setter
    def day(self, day: int) -> None:
        if Date.checkData(day=day):
            self.__day = day
        else:
            raise ValueError

    @year.setter
    def year(self, year: int) -> None:
        if Date.checkData(year=year):
            self.__year = year
        else:
            raise ValueError

    @month.setter
    def month(self, month: int) -> None:
        if Date.checkData(month=month):
            self.__month = month
        else:
            raise ValueError
