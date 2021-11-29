def my_add (a, b):
    try:
        return int(a) + int(b)
    except TypeError:
        return None
    except ValueError:
        return None

print(my_add(input("Введит первое число: "), input("Введит второе число: ")))