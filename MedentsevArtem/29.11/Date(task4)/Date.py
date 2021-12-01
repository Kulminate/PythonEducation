# 4) * Создать класс Date, который имеет следующие поля:
# 		- день
# 		- месяц
# 		- год
#
# 		Все поля должны быть помечены модификатором private
# 		- реализовать доступ к полям через методы set и get
# 		-* реализовать статический метод checkData(int day, int month, int year),
# 		который проверяет существование введенной даты
# 		-* использовать проверку checkData, при попытке изменить поле метод set,
# 		в случае ошибки не проводить изменение, а вывести сообщение об ошибке на консоль
# 		-** реализовать метод differenceIdDays(day: int, month: int, year: int), который
# 		принимает другую дату и вычисляет разницу в днях между датами
# 		- протестировать работу методов
from datetime import timedelta
class Date():
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d):
        self.__d = d

    def get_d(self):
        return self.__d

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, m):
        self.__m = m

    def get_m(self):
        return self.__m

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def set(self, d, m, y):
        if self.checkData(d, m, y):
            return True
        else:
            raise ValueError('incorrect data')

    def get_y(self):
        return self.__y

    @staticmethod
    def checkData(self) -> int:
        if not self.d or not self.m or not self.y:
            raise UnboundLocalError('Not enough data.')
        else:
            return True

    def differenceIdDays(self, other):
        if self.checkData(self) and other.checkData(other):
            a = timedelta(days=(self.d+self.m*30+self.y*365)) - timedelta(days=(other.d+other.m*30+other.y*365))
            time = a.days
            print(time)
            yy = time//365
            time -= yy*365
            mm = time//31
            time -= mm*31
            return f'{yy} г. {mm} м. {time} д.'
