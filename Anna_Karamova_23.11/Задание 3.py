# Задание3. Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items передайте в написанную вами функцию,
# которая создает и возвращает новый словарь,
# "обратный" исходному, т. е. ключами являются строки, а значениями – числа.

def reverse(dictItems):
    return_value = {}
    for key, value in dictItems:
        return_value[value] = key
    return return_value


def reverse2(dictItems):
    return {value: key for (key, value) in dictItems}


dict_1 = {
    1: "apple",
    2: "banana",
    3: "orange",
    4: "kiwi"
}
dict_items = dict_1.items()
print("Оригинальный словарь:\n", dict_1)

print("Словарь модифицированный первым способом:\n", reverse(dict_items))
print("Словарь модифицированный вторым способом:\n", reverse2(dict_items))
