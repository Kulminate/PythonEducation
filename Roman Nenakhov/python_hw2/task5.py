# У вас есть такой треугольник, он бесконечен
#               1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Вы должны написать цикл, который будет высчитывать какая сумма цифр на указанной стороке, например:
# (Input --> Output)
#
# 1 -->  1
# 2 --> 3 + 5 = 8

line_number = int(input("Введите номер строки: "))

current_number = 1
stop = 2
result = list()

for i in range(0, line_number):
    result = list()
    for column in range(1, stop):
        print(current_number, end=' ')
        result.append(current_number)
        current_number += 2
    print(" ")
    stop += 1

print("Сумма чисел указанной строки: ", sum(result))
