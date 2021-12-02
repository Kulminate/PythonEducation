from Date import Date
from datetime import datetime


class DateTime(Date):
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:
        super().__init__(year, month, day)
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @hour.setter
    def hour(self, value):
        self._hour = value

    @minute.setter
    def minute(self, value):
        self._minute = value

    @second.setter
    def second(self, value):
        self._second = value

    @staticmethod
    def checkTime(hour: int, minute: int, second: int):
        try:
            datetime(year=2000, month=12, day=15, hour=hour, minute=minute, second=second)
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def checkDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int):
        if Date.checkData(year, month, day) and DateTime.checkTime(hour, minute, second):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

    def nextSecond(self):
        self._second += 1

    def nextMinute(self):
        self._minute += 1

    def nextHour(self):
        self._hour += 1
