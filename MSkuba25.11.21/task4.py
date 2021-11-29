# 4) Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12)
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).




def season(monthNum=input("Enter month number: ")):

        monthNum = int(monthNum)
        mList = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
                      'autumn', 'autumn', 'autumn', 'winter']

        if monthNum <= 12:
            return mList[monthNum-1]
        elif monthNum == 1 :
            return mList[monthNum - 1]
        elif monthNum > 1 :
            return mList[monthNum-1]






print(season())


# def seasonm (m=input("input")):
#
#     if m == 12:
#         return "winter"
#     elif m == 1:
#         return "winter"
#     elif m == 2:
#         return "winter"
#     elif m == 3:
#         return "spring"
#     elif m == 4:
#         return "spring"
#     elif m == 5:
#         return "spring"
#     elif m == 6:
#         return "summer"
#     elif m == 7:
#         return "summer"
#     elif m == 8:
#         return "summer"
#     elif m == 9:
#         return "autumn"
#     elif m == 10:
#         return "autumn"
#     elif m == 11:
#         return "autumn"
#     else:
#         return "false"
#     print(season(m))

# spring =[3,4,5]
    # summer =[6,7,8]
    # autumn =[9,10,11]

# s = {"winter": (12, 1, 2),
 #      "spring": (3, 4, 5),
 #     "summer":(6, 7, 8),
 #     "autumn":(9, 10, 11)
 #      }
 #



# winter = ["December", "January", "February"]
# spring = ["March", "April", "May"]
# summer = ["June", "July", "August"]
 # autumn = ["September", "October", "November"]
 # if month in winter:
 #     return winter
 # elif month in spring:
 #     return spring
 # elif month in summer:
#     return summer
# elif month in autumn:
#     return autumn
