class Date:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if Date.check_data(day=day):
            self.__day = day
        else:
            raise ValueError('Day value incorrect')
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if Date.check_data(month=month):
            self.__month = month
        else:
            raise ValueError('Month value incorrect')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if Date.check_data(year=year):
            self.__year = year
        else:
            raise ValueError('Year value incorrect')

    def __str__(self):
        if 1 <= self.__month <= 9:
            return f'{self.day}.0{self.__month}.{self.__year}'
        else:
            return f'{self.day}.{self.__month}.{self.__year}'

    @staticmethod
    def check_data(day: int = 1, month: int = 1, year: int = 1):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
            print('Date is valid')
            return True
        else:
            print('Date is invalid')
            return False

    def difference_id_days(self, day: int, month: int, year: int ):
        self.__day -= day
        self.__month -= month
        self.__year -= year
        if self.check_data(self.__day, self.__month, self.__year) == True:
            return self
        else:
            raise IndexError('Date out of range')