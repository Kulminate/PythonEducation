def arithmetic (a, b, x):
    if a.isdigit() and b.isdigit:
        return main(int(a), int(b), x)
    else:
        return float_number_checker(a, b, x)


def float_number_checker(a, b, x):
    try:
        a, b = float(a), float(b)
        main(a, b, x)
    except ValueError:
        return 'Первые два значения должны быть числами'


def main(a, b, x):
    try:
        if x == '+':
            return a + b
        elif x == '-':
            return a - b
        elif x == '*':
            return a * b
        elif x == '/':
            return a / b
        else:
            return "Неизвестная операция"
    except ZeroDivisionError:
        return'Деление на ноль недопустимо'


print(arithmetic('1', '0', '/'))

