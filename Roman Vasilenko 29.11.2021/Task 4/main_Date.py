from Date import Date

if __name__ == '__main__':

    birthday = Date(23, 5, 2000)
    print(birthday)
    birthday = Date(23, 11, 2000)
    print(birthday)

    Date.check_data(23, 5, 2000)
    Date.check_data(55, 45, 105)

    birthday.difference_id_days(2, 2, 222)
    #birthday.difference_id_days(2222, 2222, 222222)
    print(birthday)