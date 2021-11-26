def arithmetic(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "Неизвестная операция"


a = int(input("введите число a\n"))
b = int(input("введите число \n"))
c = input("введите операцию (+, -, *, / )\n")
print(arithmetic(a, b, c))
