from Date import Date

class DateTime(Date):
    def __init__(self, y: int, m: int, d: int, h: int, minute: int, s: int):
        super().__init__(y, m, d)
        self.h = h
        self.minute = minute
        self.s = s

    def __str__(self):
        if int(self._m) < 10:
            self._m = '0' + str(self._m)
        if int(self._d) < 10:
            self._d = '0' + str(self._d)
        if int(self._h) < 10:
            self._h = '0' + str(self._h)
        if int(self._minute) < 10:
            self._minute = '0' + str(self._minute)
        if int(self._s) < 10:
            self._s = '0' + str(self._s)
        return f'{self._y}-{self._m}-{self._d} {self._h}:{self._minute}:{self._s}'

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h: int):
        if self.checkTime(h, 'h'):
            self._h = h

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute: int):
        if self.checkTime(minute, 'minute'):
            self._minute = minute

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, s: int):
        if self.checkTime(s, 's'):
            self._s = s

    @staticmethod
    def checkTime(h=None, minute=None, s=None) -> int:
        if minute == 'h':
            minute = None
        elif minute == 'minute':
            minute = h
            h = None
        elif minute == 's':
            s = h
            h = None
            minute = None
        if not h and not minute and not s and h != 0 and minute != 0 and s != 0:
            raise UnboundLocalError('Not enough data.')
        else:
            if h is not None and type(h) != Date:
                try:
                    if int(h) > 24:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if minute is not None:
                try:
                    if int(minute) > 59:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if s is not None:
                try:
                    if int(s) > 59:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')

        return True

    def checkDateTime(y=None, m=None, d=None, h=None, minute=None, s=None):
        if m == 'y':
            m = None
        elif m == 'm':
            m = y
            y = None
        elif m == 'd':
            d = y
            y = None
            m = None
        elif m == 'h':
            h = y
            y = None
            m = None
        elif m == 'minute':
            minute = y
            y = None
            m = None
        elif m == 's':
            s = y
            y = None
            m = None
        if not y and not m and not d and not h and not minute and not s and y != 0 and m != 0 and d != 0 and h != 0 and minute != 0 and s != 0:
            raise UnboundLocalError('Not enough data.')
        else:
            if y is not None and type(y) != Date:
                try:
                    if int(y) > 2200:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if m is not None and type(m) != Date:
                try:
                    if int(m) > 12:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if d is not None and type(d) != Date:
                try:
                    if int(d) > 31:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if h is not None and type(h) != Date:
                try:
                    if int(h) > 24:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if minute is not None and type(minute) != Date:
                try:
                    if int(minute) > 59:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
            if s is not None and type(s) != Date:
                try:
                    if int(s) > 59:
                        raise ValueError('Incorrect data.')
                except TypeError:
                    raise ValueError('Incorrect data.')
        return True

    def nextSecond(self):
        self._s += 1
        if self._s >= 60:
            self._s = 0
            self.nextMinute()

    def nextMinute(self):
        self._minute += 1
        if self._minute >= 60:
            self._minute = 0
            self.nextHour()

    def	nextHour(self):
        self._h += 1
        if self._h >= 24:
            self._h = 0
            self._DateTime__nextDay()

    def __nextDay(self):
        self._d += 1
        if self._d >= 32:
            self._d = 0
            self._DateTime__nextMonth()

    def __nextMonth(self):
        self._m += 1
        if self._m >= 13:
            self._m = 0
            self._DateTime__nextYear()



    def __nextYear(self):
        self._y += 1
        if self._y >= 2200:
            print('Are you going back to the future, Marty McFly?')



