# 3. Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items передайте в
# написанную вами функцию, которая создает и возвращает новый словарь, "обратный"
# исходному, т. е. ключами являются строки, а значениями – числа.

def reverse_dict(dict_items):
    reversed_dict = {}
    for pair in dict_items:
        reversed_dict.setdefault(pair[1], pair[0])
    return reversed_dict


d = {1: "one", 2: "two", 3: "three"}
dict_items = d.items()
print(reverse_dict(dict_items))
