# Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items
# передайте в написанную вами функцию, которая создает и возвращает новый словарь,
# "обратный" исходному, т. е. ключами являются строки, а значениями – числа.


def reverse_dict(old_dict):
    new_dict = dict(zip(old_dict.values(), old_dict.keys()))
    return new_dict


my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
dict_items = my_dict.items()

print(reverse_dict(my_dict))
