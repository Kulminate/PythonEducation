# 4. Дан словарь. { 'a': 11, 'b’:12, 'c': 17, 'd': 23, 'e':12 }
# Нужно написать функцию,
# которая возвращает список имен ключей, чьи значения попадают в диапазон (x,y)
def val_of_keys_in_range(d, a, b):
    res_values = []
    if a < b:
        low, high = a, b
    else:
        low, high = b, a
    for key in d.keys():
        if low <= d[key] <= high:
            res_values.append(key)
    return res_values


d = {'a': 11, 'b': 12, 'c': 17, 'd': 23, 'e': 12}
a = int(input("Введите начало диапазона\n"))
b = int(input("Введите конец диапазона\n"))
print(val_of_keys_in_range(d, a, b))
