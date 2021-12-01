# 4) *Создать класс Date, который имеет следующие поля:
# - день
# - месяц
# - год
# Все поля должны быть помечены модификатором private - реализовать доступ к полям через методы set и get
# - *реализовать статический метод checkData(int day, int month, int year), который проверяет существование введенной
# даты
# - *использовать проверку checkData, при попытке изменить поле метод set, в случае ошибки не проводить изменение, а
# вывести сообщение об ошибке на консоль
# - ** реализовать метод differenceIdDays(day: int, month: int, year: int), который принимает другую дату
# и вычисляет разницу в днях между датами
# - протестировать работу методов
from datetime import time, datetime, timedelta, date
class Date:
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year


    @property
    def day(self)-> int:
        return self.__day

    @day.setter
    def day(self, day:int)-> None:
        try:
            if Date.checkData(day,self.__month,self.__year): #проверка checkData
                self.__day = day
            else: print("Такой даты не существует")
        except ValueError as e:
            print(e)

    @property
    def month(self) -> int:
        return self.__month

    @month.setter
    def month(self, month:int) -> None:
        try:
            if Date.checkData(self.__day, month, self.__year): #проверка checkData
                self.__month = month
            else: print("Такого месяца не существует")

        except ValueError as e:
            print(e)

    @property
    def year(self)-> int:
        return self.__year

    @year.setter
    def year(self, year:int)-> None:
        try:
            if Date.checkData(self.__day, self.__month, year): #проверка checkData
                self.__year = year
            else: print("Такого года не существует")
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
            date2 = date(self.__year, self.__month, self.__day)
            if date1 <date2:
                date1,date2=date2,date1
            count_days = date1-date2
            print("Разница в днях:",count_days)
        else: return "Даты не существует"



if __name__ == '__main__':

    date1 = Date(12,3,2012)
    print(date1.month)
    date1.day= 40 # метод set
    print(date1.day)
    date1.month = 12 # метод set
    date1.year = 2012 # метод set
    print(date1.day, date1.month, date1.year)
    print(Date.checkData(12, 2, 2011))  # статический метод checkData(int day, int month, int year)
    date1.differenceIdDays(11,11,2012) # метод differenceIdDays(self, day: int, month: int, year: int)




