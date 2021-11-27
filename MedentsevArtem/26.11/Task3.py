# 3) Написать функцию my_add (), которая принимает два аргумента.
# Если аргументы можно сложить, возвращается сумма. Если сложение
# аргументов вызовет ошибку, функция должна вместо этого вернуть None.
# Если есть различные исключения - то их обрабатывать отдельно
def my_add(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        try:
            return a + b
        except TypeError:
            return None


print(my_add(input('Enter first value:'), input('Enter second value:')))