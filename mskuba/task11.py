k = "*"
e = " "


def star(n):
    for i in range(n):
        print((n - i - 5) * e + (i + i + 1) * k)


def star2(n):
    for i in range(n):
        print((n - i - 1) * e + (i + i + 1) * k)

    for i in range(5):
        print(k * i)
    for i in range(3, 0, -1):
        print(k * i)

# Сложно, буду учить!


star(5)
star2(5)
