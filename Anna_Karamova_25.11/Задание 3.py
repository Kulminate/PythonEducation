#Задание3) Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
#с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def calcSquare(edge: float) -> tuple[float, float, float]:
    return tuple([edge * 4,
                  edge * edge,
                  math.sqrt(2) * edge])


edge: float = float(input("Введите длину стороны квадрата:").strip())
perimeter, square, diagonal = calcSquare(edge)
print(f"Периметр квадрата {perimeter} площадь {square} диагональ {diagonal}")
