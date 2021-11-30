#Задание 4
# Дан словарь. { 'a': 11, 'b’:12, 'c': 17, 'd': 23, 'e':12 }
#Нужно написать функцию, которая возвращает список имен ключей, чьи значения попадают в диапазон (x,y)
#dict_1 = {'a': 11, 'b’:12, 'c': 17, 'd': 23, 'e':12 }

dict_1 = {'a': 11, 'b':12, 'c': 17, 'd': 23, 'e':12 }
x = 15
y = 25

def keysInRange(dict):
    for i in dict:
        if dict.setdefault(i) >= x and dict.setdefault(i) <= y:
            print(i)

keysInRange(dict_1)