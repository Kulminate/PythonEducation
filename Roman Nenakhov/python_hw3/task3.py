# Написать функцию square, принимающую 1 аргумент
# — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side):
    return side * 4, side ** 2, side * (2 ** 0.5)


print(square(int(input("Введите сторону квадрата: "))))