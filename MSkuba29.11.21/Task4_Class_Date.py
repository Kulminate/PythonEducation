
from datetime import  datetime,  date

class Date:
    def __init__(self, day:int, month:int, year:int):
        self._day = day
        self._month = month
        self._year = year


    @property
    def day(self)-> int:
        return self._day

    @day.setter
    def day(self, day:int)-> None:
        try:
            if Date.checkData(day, self._month, self._year):
                self._day = day
            else: print("Incorrect Date ")
        except ValueError as e:
            print(e)

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, month:int) -> None:
        try:
            if Date.checkData(self._day, month, self._year):
                self._month = month
            else: print("Incorrect month")

        except ValueError as e:
            print(e)

    @property
    def year(self)-> int:
        return self._year

    @year.setter
    def year(self, year:int)-> None:
        try:
            if Date.checkData(self._day, self._month, year):
                self._year = year
            else: print("Incorrect year")
        except ValueError as e:
            print(e)

    @staticmethod
    def checkData(day:int, month:int, year:int):
        date = str(day)+'/'+ str(month)+'/'+str(year)
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except: return False



    def differenceIdDays(self, day: int, month: int, year: int):
        if Date.checkData(day,month,year):
            date1 = date(year, month, day)
            date2 = date(self._year, self._month, self._day)
            if date1 < date2:
                date1, date2 = date2, date1
            count_days = date1-date2
            print("days interval:",count_days.days)
        else: return "The date not exist"





