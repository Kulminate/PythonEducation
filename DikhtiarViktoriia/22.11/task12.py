a = int(input("Введите число: "))
b = int(input("Введите число: "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)