# Задание 2. Вы принимаете от пользователя последовательность чисел, разделённых запятой.
#Составьте список и кортеж с этими числами.
input_list = (input("Введите последовательность чисел для списка:"))
list_1 = input_list.split(',')
trimmed_list = []
for item in list_1:
    trimmed_list.append(item.strip())

print("Ваш список с элементами без пробелов:", trimmed_list)
list_2 = tuple(trimmed_list)
print("Ваш кортеж:",list_2)