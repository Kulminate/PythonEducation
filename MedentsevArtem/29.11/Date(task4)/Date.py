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
    def __init__(self, y: int, m: int, d: int):
        self.y = y
        self.m = m
        self.d = d

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        if self.checkData(y, 'y'):
            self._y = y

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, m: int):
        if self.checkData(m, 'm'):
            self._m = m

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, d: int):
        if self.checkData(d, 'd'):
            self._d = d

    @staticmethod
    def checkData(y=None, m=None, d=None) -> int:
        if m =='y':
            m = None
        elif m == 'm':
            m = y
            y = None
        elif m == 'd':
            d = y
            y = None
            m = None
        if not d and not m and not y and d != 0 and m != 0 and y != 0:
            raise UnboundLocalError('Not enough data.')
        else:
            if d is not None and type(d) != Date:
                try:
                    if int(d) > 31:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if m is not None and type(m) != Date:
                try:
                    if int(m) > 12:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if y is not None and type(y) != Date:
                try:
                    if int(y) > 2200:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
        return True

    def differenceIdDays(self, other) -> str:
        if self.checkData(self) and other.checkData(other):
            a = timedelta(days=(int(self._d)
                                + int(self._m) * 30
                                + int(self._y) * 365)) \
              - timedelta(days=(int(other._d)
                                + int(other._m) * 30
                                + int(other._y) * 365))
            time = a.days
            yy = time // 365
            time -= yy * 365
            mm = time // 31
            time -= mm * 31
            return f'{abs(yy)} г., {abs(mm)} м., {abs(time)} д.'
