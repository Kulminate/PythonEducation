def arithmetic(a, b, f):
    if f == "+":
        return a + b
    elif f == "-":
        return a - b
    elif f == "/":
        return a / b
    elif f == "*":
        return a * b
    else:
        return "Неизвестная операция"

print(arithmetic(4, 2, "+"))