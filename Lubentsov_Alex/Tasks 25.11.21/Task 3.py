#  3) Написать функцию square, принимающую 1 аргумент — сторону квадрата,
#  и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

def square(storona_kvadrata):
    return (4 * storona_kvadrata, storona_kvadrata ** 2, (2 * storona_kvadrata ** 2) ** .5)

result = square(int(input("Введите сторону квадрата: ")))

print(result)