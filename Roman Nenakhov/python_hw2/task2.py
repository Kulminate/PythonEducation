# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.
numbers = input("Пожалуйста введите последовательность чисел через запятую: ")

list_of_numbers = [int(i) for i in (numbers.split(','))]
print("Список: ", list_of_numbers)

tuple_of_numbers = tuple(list_of_numbers)
print("Кортеж: ", tuple_of_numbers)
