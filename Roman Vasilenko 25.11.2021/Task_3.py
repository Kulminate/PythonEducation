# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square(side = input('Enter a value for the side of the square: \n')):
    try:
        side = int(side)

        if side < 0:
            return 'side must be positive number'

        perimeter = side * 4
        squared = side ** 2
        diagonal = (2 * (side ** 2)) ** 0.5  #d=√(2a2)
        return perimeter, squared, diagonal
    except (TypeError, ValueError):
        print('Enter correct value!')


print(square())

