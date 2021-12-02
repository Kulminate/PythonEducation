import datetime
from Date import Date


class Datetime(Date):
    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(year, month, day)
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @staticmethod
    def checkDatetime(year, month, day, hour, minute, second):
        datetime.datetime(year, month, day, hour, minute, second)

    # Переопределенный сеттер
    @Date.day.setter
    def day(self, new_day):
        Date.checkDatetime(self.year, self.month, new_day, self.hours, self.minutes, self.seconds)
        self.__day = new_day

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        Date.checkDatetime(self.year, self.month, self.day, value, self.minutes, self.seconds)
        self.__hours = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        Date.checkDatetime(self.year, self.month, self.day, self.hours, value, self.seconds)
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        Date.checkDatetime(self.year, self.month, self.day, self.hours, self.minutes, value)
        self.__seconds = value

    def __str__(self):
        # pad with particular number of zeroes
        return f"{self.year:04}-{self.month:02}-{self.day:02} {self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    @staticmethod
    def fromSystemDatetime(sd: datetime.datetime) -> 'Datetime':
        return Datetime(sd.year, sd.month, sd.day, sd.hour, sd.minute, sd.second)

    def nextSecond(self, seconds=1) -> 'Datetime':
        return Datetime.fromSystemDatetime(self.getDatetime() + datetime.timedelta(seconds=seconds))

    def nextHours(self, hours=1) -> 'Datetime':
        return Datetime.fromSystemDatetime(self.getDatetime() + datetime.timedelta(hours=hours))

    def nextMinutes(self, minutes=1) -> 'Datetime':
        return Datetime.fromSystemDatetime(self.getDatetime() + datetime.timedelta(minutes=minutes))

    def getDatetime(self) -> datetime.datetime:
        return datetime.datetime(self.year, self.month, self.day, self.hours, self.minutes, self.seconds)


if __name__ == '__main__':
    date = Datetime(year=2021, month=12, day=1, hours=21, minutes=28, seconds=15)

    print(f"An hour and 15 minutes after \'{date}\' is \'{date.nextHours().nextMinutes(15)}\'")
