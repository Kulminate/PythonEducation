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
from datetime import time, datetime, timedelta
class Date:
    def __init__(self, date:int, month:int, year:int):
        self.__date = date
        self.__month = month
        self.__year = year

    def print(self):
        print(f"{self.__date}/{self.__month}/{self.__year}")

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        try:
            self.__date = int(date)
        except ValueError as e:
            print(e)

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        try:
            self.__month = int(month)
        except ValueError as e:
            print(e)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        try:
            self.__year = int(year)
        except ValueError as e:
            print(e)
    @staticmethod
    def checkData(day:int, month:int, year:int):
        date = str(day)+'/'+ str(month)+'/'+str(year)
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except Exception as e: return e



    # def differenceIdDays(self, day: int, month: int, year: int):
    #     # date1 = str(day) + '/' + str(month) + '/' + str(year)
    #     date2 = str(self.__date) + '/' + str(self.__month) + '/' + str(self.__year)
    #     try:
    #         if date1 < date2:
    #             date1 = timedelta(days=-day, month=-month, year=-year)
    #             date2 = time.strptime(date2, '%d/%m/%Y')
    #             return (date2 - date1).strftime("%d/%m/%Y")
    #     except: raise "Введенной даты не существует"




if __name__ == '__main__':

    date1 = Date(12,3,2012)
    date1.date = 12 # метод set
    date1.month = 12 # метод set
    date1.year = 2012 # метод set
    print(Date.checkData(30, 2, 2012))  # статический метод checkData(int day, int month, int year)
    # print(Date.checkData(date1.date,date1.month,date1.year))




