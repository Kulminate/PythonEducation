# Написать функцию my_add (), которая принимает два аргумента. Если аргументы можно сложить, возвращается сумма.
# Если сложение аргументов вызовет ошибку, функция должна вместо этого вернуть None.
# Если есть различные исключения - то их обрабатывать отдельно

def my_add(arg1=input('Enter first argument: '), arg2=input('Enter first argument: ')):
    try:
        result = eval(f'{arg1} + {arg2}')
        return f'{arg1} + {arg2} = {result}'
    except:
        return None

print(my_add())