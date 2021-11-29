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
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    def __str__(self):
        if 1 <= self.__month <= 9:
            return f'{self.day}.0{self.__month}.{self.__year}'
        else:
            return f'{self.day}.{self.__month}.{self.__year}'

    @staticmethod
    def check_data(day: int, month: int, year: int):
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