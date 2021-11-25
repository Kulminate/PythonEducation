# Нарисовать треугольник заданной размерности.

a = int(input())

for i in range(1, a + 1):
    print("* " * i)


for i in range(1, a + 1):
    num = 1
    for j in range(a, 0, -1):
        if j > i:
            print(" ", end="")
        else:
            print(" *", end="")
            num += 1
    print("")


for i in range(1, a+1):
    if i <= a//2+1:
        for j in range(i):
            print("*", end='')
    elif i > a//2+1:
        for j in range(0, a-i+1):
            print('*', end="")
    print()
