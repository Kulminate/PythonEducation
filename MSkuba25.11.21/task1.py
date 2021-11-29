#1) Написать функцию arithmetic, принимающую 3 аргумента: первые 2 -
# числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".
def arithmetic(a,b,c):
    a = int(input("inptut numb"))
    b = int(input("inptut numb"))
    c = str(input("math act +,-,*,/"))
    if c =="+":
        return a+b
    elif  c =="-":
        return a-b
    elif c =="*":
        return a * b
    elif c =="/":
        return a/b
    else:
        return "Неизвестная операция"
print(arithmetic("a","b","c"))






