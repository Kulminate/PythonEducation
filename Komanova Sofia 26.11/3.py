# 3) Написать функцию my_add (), которая принимает два аргумента.
# Если аргументы можно сложить, возвращается сумма. Если сложение аргументов вызовет ошибку,
# функция должна вместо этого вернуть None.
# Если есть различные исключения - то их обрабатывать отдельно
def my_add(a,b):
    try:
        s = a+b
        print( 'Сумма двух чисел равна:', s)
    # except TypeError:
    #     print("Операция применена к объекту несоответствующего типа")
    except Exception:
        return None



my_add(2, 5)
print(my_add(4, 'dfsf'))


