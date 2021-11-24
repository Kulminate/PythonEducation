# Дан словарь. { 'a': 11, 'b’:12, 'c': 17, 'd': 23, 'e':12 }
# Нужно написать функцию, которая возвращает список имен ключей,
# чьи значения попадают в диапазон (x,y)

def name_keys(old_dict, x, y):
    result = list()
    if x > y:
        temp = x
        x = y
        y = temp
    for k, v in old_dict.items():
        for item in range(x, y + 1):
            if v == item:
                result.append(k)
    return result


my_dict = {'a': 11, "b": 12, 'c': 17, 'd': 23, 'e': 12}
print(name_keys(my_dict, 1, 12))
