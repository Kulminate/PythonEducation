# 4) Берем класс Date из предыдущего домашнего задания.
# Реализовать класс DateTime, который наследуется от класса Date.
# 		В нем должны быть дополнительные поля
# - часы
# - минута
# - секунда
# доступ к полям должен быть через get/set
# реализовать статический метод checkTime(int hour, int minute, int second), который проверяет существование
# введенной даты
# реализовать статический метод checkDateTime(int day, int month, int year, int hour, int minute, int second),
# который проверяет существование введенной даты
# - реализовать методы
# 			nextSecond();
# 			nextMinute();
# 			nextHour();
# которые увелечивают на единицу значение секунды, минуты и часа соответственно,
# при чем если кол-во часов достигается 24, то должно увеличиться на единицу значение поля day из базового класса

from Komanova_Sofia_29_11.task4 import Date
from datetime import timedelta, datetime

class DateTime(Date):
    # 		В нем должны быть дополнительные поля
    # - часы
    # - минута
    # - секунда
    def __init__(self, day:int, month:int, year:int, hour:int, minute:int, seconds:int):
        super().__init__(day, month, year)
        self.__hour = hour
        self.__min = minute
        self.__sec = seconds

    # @property
    # def day(self):
    #     super().day



    # доступ к полям должен быть через get/set
    @property
    def hour(self) -> int:
        return self.__hour

    @hour.setter
    def hour(self, h:int)->None:
        self.__hour = h

    @property
    def minutes(self) -> int:
        return self.__min

    @minutes.setter
    def minutes(self, m: int) -> None:
        self.__min = m

    @property
    def sec(self) -> int:
        return self.__sec

    @sec.setter
    def sec(self, s: int) -> None:
        self.__sec = s

    # реализовать статический метод checkTime(int hour, int minute, int second), который проверяет существование
    # введенной даты
    @staticmethod
    def checkTime(hour:int, minute:int, second:int):
        date = str(hour) + ':' + str(minute) + ':' + str(second)
        try:
            datetime.strptime(date, '%H:%M:%S')
            print("Введенное время существует")
            return True
        except:
            print("Введенное время не существует")
            return False

    # реализовать статический метод checkDateTime(int day, int month, int year, int hour, int minute, int second),
    # который проверяет существование введенной даты
    @staticmethod
    def checkDateTime(day:int, month:int, year:int, hour:int, minute:int, second:int):
        date = str(day) + ':'+ str(month) + ':'+ str(year) + ':'+ str(hour) + ':' + str(minute) + ':' + str(second)
        try:
            date = datetime.strptime(date, '%d:%m:%Y:%H:%M:%S')
            print(f"Введенная дата {date} существует")
            return True
        except:
            print("Введенной даты не существует")
            return False

    # - реализовать методы
    # 			nextSecond();
    # 			nextMinute();
    # 			nextHour();
    # которые увелечивают на единицу значение секунды, минуты и часа соответственно,
    # при чем если кол-во часов достигается 24, то должно увеличиться на единицу значение поля day из базового класса
    def next_second(self):
        time = timedelta(days=self.day, hours= self.__hour, minutes=self.__min, seconds=self.__sec)
        nextsec = time + timedelta(seconds=1)
        print(f"Время на секунду дольше {time} - {nextsec}")
        return nextsec

    def next_minute(self):
        time = timedelta(days=self.day, hours= self.__hour, minutes=self.__min, seconds=self.__sec)
        nextmin = time + timedelta(minutes=1)
        print(f"Время на минуту дольше {time} - {nextmin}")
        return nextmin

    def next_hour(self):
        time = timedelta(days=self.day, hours= self.__hour, minutes=self.__min, seconds=self.__sec)
        nexthour = time + timedelta(hours=1)
        print(f"Время на час дольше {time} - {nexthour}")
        return nexthour

    # переопределить метод __str___ для печати DateTime таким видом - 2020-11-30 19:55:55
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day} {self.__hour}:{self.__min}:{self.__sec}'








if __name__ == '__main__':
        first = DateTime(20,11,2011,23,34,60)
        # first.month= 3
        # print(first.month)
        print("checkTime:")
        DateTime.checkTime(12,12,12)
        print("checkTime:")
        DateTime.checkTime(12, 123, 12)
        print("checkDateTime:")
        DateTime.checkDateTime(12,12,1221,3,2,12)
        print("checkDateTime:")
        DateTime.checkDateTime(12, 30, 1221, 3, 2, 12)
        first.next_second()
        first.next_minute()
        first.next_hour()
        print("переопределить метод __str__ –", first)






