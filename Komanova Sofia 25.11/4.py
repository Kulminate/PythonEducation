# 4) Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
def season(month):
    if month in [12,1,2]:
        print("зима")
    if month in [3,4,5]:
        print("весна")
    if month in [6,7,8]:
        print("лето")
    if month in [9,10,11]:
        print("осень")

season(int(input()))
