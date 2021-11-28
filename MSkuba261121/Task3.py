# 3) Написать функцию my_add (), которая принимает два аргумента.
# Если аргументы можно сложить, возвращается сумма.
# Если сложение аргументов вызовет ошибку, функция должна вместо этого вернуть None.
# Если есть различные исключения - то их обрабатывать отдельно


def my_add(a=int(input("введите первое значение")), b=int(input("введите второе значение"))):
    try:
        c = a + b
        print(c)

    except TypeError:

        return None
    except ValueError:
        return None
    # except Exception:
    #     return None


#
# my_add(10, 20)
print(my_add())
