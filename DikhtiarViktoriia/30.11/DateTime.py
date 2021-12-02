from DikhtiarViktoriia.b29_11.Date import Date
import datetime

class DateTime(Date):
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        super().__init__(year, month, day)
        self._hour = hour
        self._minute = minute
        self._second = second

    def __str__(self):
        return f"{self._year}-{self._month}-{self._day} {self._hour}:{self._minute}:{self._second}"

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, h: int):
        self._hour = h

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, m: int):
        self._minute = m

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, s: int):
        self._second = s

    @staticmethod
    def checkTime(_hour: int, _minute: int, _second: int):
        try:
            return datetime.time(_hour, _minute, _second)
        except ValueError as e:
            print(e)

    @staticmethod
    def checkDateTime(_year: int, _month: int, _day: int, _hour: int, _minute: int, _second: int):
        try:
            return datetime.datetime(_year, _month, _day, _hour, _minute, _second)
        except ValueError as e:
            print(e)

    def next_second(self):
        t1 = datetime.timedelta(days=self.day, hours= self._hour, minutes=self._minute, seconds=self._second)
        sec = t1 + datetime.timedelta(seconds=1)
        return f"{t1}, {sec}"

    def next_minute(self):
        t1 = datetime.timedelta(days=self.day, hours= self._hour, minutes=self._minute, seconds=self._second)
        min = t1 + datetime.timedelta(minutes=1)
        return f"{t1}, {min}"

    def next_hour(self):
        t1 = datetime.timedelta(days=self.day, hours= self._hour, minutes=self._minute, seconds=self._second)
        h = t1 + datetime.timedelta(hours=1)
        return f"{t1}, {h}"




t = DateTime(2012, 3, 12, 23, 23, 14)
print(DateTime.checkTime(26, 3, 12))
print(DateTime.checkDateTime(2012, 3, 12, 13, 23, 14))
print(t.next_second())
print(t.next_minute())
print(t.next_hour())