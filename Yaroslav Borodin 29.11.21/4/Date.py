import datetime


class Date:

    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def checkData(day=9, month=12, year=1999) -> bool:
        try:
            datetime.date(year, month, day)
        except ValueError:
            print("Некорректная дата")
            return False
        else:
            print("Корректная дата")
            return True

    def differenceIdDays(self, day: int, month: int, year: int) -> int:
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
