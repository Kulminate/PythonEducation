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

    # - ** реализовать
    # метод differenceIdDays(day: int, month: int, year: int), который принимает другую
    # дату и вычисляет разницу в днях между датами
    def differenceIdDays(self, day: int, month: int, year: int) -> datetime:
        self_td = datetime.timedelta(self.__year, self.__month, self.__day)
        print(self_td)
        other_td = datetime.timedelta(year, month, day)
        print(other_td)
        return (self_td - other_td).days

    @property
    def day(self) -> int:
        return self._day

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @day.setter
    def day(self, day: int) -> None:
        if Date.checkData(day=day):
            self._day = day
        else:
            raise ValueError

    @year.setter
    def year(self, year: int) -> None:
        if Date.checkData(year=year):
            self._year = year
        else:
            raise ValueError

    @month.setter
    def month(self, month: int) -> None:
        if Date.checkData(month=month):
            self._month = month
        else:
            raise ValueError
