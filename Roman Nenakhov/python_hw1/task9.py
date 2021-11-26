# Сложите цифры целого числа.

def sum_x(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


print(sum_x(int(input())))
