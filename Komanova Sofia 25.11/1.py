# 1) Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая
# должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
# / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(a,b,c:str):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    else:
        print('Неизвестная операция')


print("Первое число: ", arithmetic(int(input()), "Второе число: ", int(input()), "Операция: ", str(input())))





