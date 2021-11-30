from Date import Date

if __name__ == '__main__':

    birthday = Date(23, 5, 2000)
    print(birthday)
    birthday = Date(23, 11, 2000)
    print(birthday)

    #Check this. Output difference Exceptions
    # date_1 = Date(55, 10, 1999)
    # date_2 = Date(20, 55, 1999)
    # date_3 = Date(20, 10, 9999999)



    Date.check_data(23, 5, 2000)
    Date.check_data(55, 45, 105)

    birthday.difference_id_days(2, 2, 222)
    #birthday.difference_id_days(2222, 2222, 222222)
    print(birthday)