# Задание 9 Сложите цифры целого числа.
number = int(input("Введите целое число:"))

sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit

    number = number // 10

print("Сумма цифр целого числа:", sum)

