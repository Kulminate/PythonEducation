class Date:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if Date.check_data(day=day):
            self._day = day
        else:
            raise ValueError('Day value incorrect')
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if Date.check_data(month=month):
            self._month = month
        else:
            raise ValueError('Month value incorrect')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if Date.check_data(year=year):
            self._year = year
        else:
            raise ValueError('Year value incorrect')

    def __str__(self):
        if 1 <= self._month <= 9:
            return f'{self.day}.0{self._month}.{self._year}'
        else:
            return f'{self.day}.{self._month}.{self._year}'

    @staticmethod
    def check_data(day: int = 1, month: int = 1, year: int = 1):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:

            return True
        else:

            raise ValueError('Data not valid')

    def difference_id_days(self, day: int, month: int, year: int ):
        self._day -= day
        self._month -= month
        self._year -= year
        if self.check_data(self._day, self._month, self._year) == True:
            return self
        else:
            raise IndexError('Date out of range')