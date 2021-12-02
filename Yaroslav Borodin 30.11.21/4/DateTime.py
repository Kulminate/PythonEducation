from Date import Date
from datetime import datetime


class DateTime(Date):
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:
        super().__init__(year, month, day)
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    @property
    def second(self) -> int:
        return self._second

    @hour.setter
    def hour(self, value: int) -> None:
        self._hour = value

    @minute.setter
    def minute(self, value: int) -> None:
        self._minute = value

    @second.setter
    def second(self, value: int) -> None:
        self._second = value

    @staticmethod
    def checkTime(hour: int, minute: int, second: int) -> bool:
        try:
            datetime(year=2000, month=12, day=15, hour=hour, minute=minute, second=second)
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def checkDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int) -> bool:
        if Date.checkData(year, month, day) and DateTime.checkTime(hour, minute, second):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

    def nextSecond(self) -> None:
        self._second += 1
        if self._second == 60:
            self._second = 0
            self.nextMinute()

    def nextMinute(self) -> None:
        self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self.nextHour()

    def nextHour(self) -> None:
        self._hour += 1
        if self._hour >= 24:
            self._hour = 1
            self._nextDay()

    def _nextDay(self) -> None:
        self.day += 1
