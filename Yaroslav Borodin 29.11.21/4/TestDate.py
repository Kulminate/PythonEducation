from Date import Date
import datetime


class TestDate:
    def __init__(self):
        pass

    @staticmethod
    def test():
        test_set1 = (({"year": 2007, "day": 15, "month": 5}, True), ({"year": 2007, "day": 36, "month": 5}, False),
                     ({"year": 2007, "day": 15, "month": 15}, False))
        print(f"Тестируем Date.checkData()")
        for i in test_set1:
            print(i[0])
            if Date.checkData(year=i[0]["year"], day=i[0]["day"], month=i[0]["month"]) == i[1]:
                print("Успешно\n")
            else:
                print("Не успешно\n")

        test_set2 = (({"year": 1995, "day": 1, "month": 5}, {"year": 1995, "day": 13, "month": 5}, 12),
                     ({"year": 2007, "day": 30, "month": 5}, {"year": 2007, "day": 12, "month": 5}, 18))
        print(f"Тестируем Date.differenceIdDays()")
        for i in test_set2:
            print(i[0], "\n", i[1])
            date1 = Date(i[0]["day"], i[0]["month"], i[0]["year"])
            if date1.differenceIdDays(i[1]["day"], i[1]["month"], i[1]["year"]) == i[2]:
                print("Успешно\n")
            else:
                print("Не успешно\n")


if __name__ == "__main__":
    TestDate.test()
