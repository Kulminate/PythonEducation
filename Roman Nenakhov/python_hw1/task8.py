# В переменных q и w хранятся два натуральных числа.
# Создайте программу, выводящую на экран результат деления q на w с остатком.

q, w = int(input()), int(input())
y = q//w
x = q%w
print(y, "- целочисленный результат деления", x, "- остаток от деления")
