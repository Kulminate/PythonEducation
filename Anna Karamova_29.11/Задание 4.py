# Задание 4) *Создать класс Date, который имеет следующие поля:
#    - день
#   - месяц
#   - год
# Все поля должны быть помечены модификатором private
#		- реализовать доступ к полям через методы set и get
# -* реализовать статический метод checkData(int day, int month, int year), который проверяет существование введенной
# даты
# -* использовать проверку checkData, при попытке изменить поле метод set, в случае ошибки не проводить изменение,
# а вывести сообщение об ошибке на консоль
#		-** реализовать метод differenceIdDays(day: int, month: int, year: int), который принимает другую дату и
# вычисляет разницу в днях между датами
#	- протестировать работу методов

import datetime


class Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, new_day):
        Date.checkDate(new_day, self.month, self.year)
        self.__day = new_day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, new_month):
        Date.checkDate(self.day, new_month, self.year)
        self.__month = new_month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        Date.checkDate(self.day, self.month, new_year)
        self.__year = new_year

    @staticmethod
    def checkDate(day, month, year):
        datetime.datetime(year, month, day)


try:
    date_1 = Date(30, 11, 2021)
    date_1.month = 13
except ValueError as error:
    print(error)
