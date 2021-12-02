from Date import Date


class DateTime(Date):

    def __init__(self, day, month, year, hour, minute, second):
        super().__init__(day, month, year)
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        # if DateTime.check_time(hour = hour) == True:
        self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        # if DateTime.check_time(minute=minute) == True:
        self._minute = minute

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        #if DateTime.check_time(second=second) == True:
        self._second = second

    @staticmethod
    def check_time(hour: int = 1, minute: int = 1, second: int = 1):
        if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:

            return True
        else:

            raise ValueError('Time not valid')

    @staticmethod
    def check_datetime(day: int = 1, month: int = 1, year: int = 1, hour: int = 1, minute: int = 1, second: int = 1):
        if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59 and 1 <= day <= 31 and 1 <= month <= 12 and \
        1 <= year <= 9999:

            return True
        else:
            return False

    def change_date(self):

        if self._second == 60:
            self._second = 0
            self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self._hour += 1
        if self._hour == 24:
            self._hour = 0
            self._day += 1
        if self._day == 32:
            self._day = 1
            self._month += 1
        if self._month == 13:
            self._month = 1
            self._year += 1

    def next_second(self):
        self._second += 1
        self.change_date()

    def next_minute(self):
        self._minute += 1
        self.change_date()

    def next_hour(self):
        self._hour += 1
        self.change_date()

    def __str__(self):
        second_null = ''
        minute_null = ''
        hour_null = ''
        day_null = ''
        month_null = ''
        if self.second <10: second_null = '0'
        if self.minute < 10: minute_null = '0'
        if self.hour < 10: hour_null = '0'
        if self.day < 10: day_null = '0'
        if self.month < 10: month_null = '0'

        return f'{self.year}-{month_null}{self.month}-{day_null}{self.day} {hour_null}{self.hour}:' \
               f'{minute_null}{self.minute}:{second_null}{self.second}'
