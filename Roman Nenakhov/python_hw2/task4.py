# Дан словарь. { 'a': 11, 'b’:12, 'c': 17, 'd': 23, 'e':12 }
# Нужно написать функцию, которая возвращает список имен ключей,
# чьи значения попадают в диапазон (x,y)

def name_keys(old_dict, x, y):
    for dict_item in old_dict.items():
        if x <= dict_item[1] <= y:
            print(dict_item[0])


my_dict = {'a': 11, "b": 12, 'c': 17, 'd': 23, 'e': 12}
name_keys(my_dict, 13, 40)

