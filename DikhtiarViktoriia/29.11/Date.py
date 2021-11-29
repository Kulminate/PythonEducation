import datetime

class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return (f"{self._year}, {self._month}, {self._day}")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, y: int):
        self._year = y

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, m: int):
        self._month = m

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, d: int):
        self._day = d

    def checkData(self, year: int, month: int, day: int):
        try:
            return datetime.date(year, month, day)
        except ValueError as e:
            print(e)

    def differenceIdDays(self, year: int, month: int, day: int):
        return (self.checkData(self._year, self._month, self._day) - datetime.date(year, month, day)).days



d = Date(2012, 5, 23)
print(d.differenceIdDays(2012, 5, 10))


# class Date:
#     def __init__(self, day: int):
#         self._day = day
#
#     def get_day(self):
#         return self._day
#
#     def set_day(self, day: int):
#         Date.checkData()
#         self._day = day
#
#     @staticmethod
#     def checkData():
#         pass
#
# d = Date(1)
# d.set_day()
# print(d.get_day())
# print()