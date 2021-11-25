# Написать функцию arithmetic, принимающую 3 аргумента:
# первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
# / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y
    else:
        err = "Неизвестная операция"
        return err


print(arithmetic(int(input()), int(input()), input()))
