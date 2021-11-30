#Задание 5
#У вас есть такой треугольник, он бесконечен
#             1
  #        3     5
 #      7     9    11
 #  13    15    17    19
#21    23    25    27    29
#...
#Вы должны написать цикл, который будет высчитывать какая сумма цифр на указанной стороке, например:
#(Input --> Output)

#1 -->  1
#2 --> 3 + 5 = 8
count_sting = int(input("Ввведите номер строки, в которую считаем:"))
string_1 = 1
number = 1
count = 0
for i in range(count_sting):
    for j in range(string_1):
        if string_1 == count_sting:
            count += number
        number += 2
    string_1 += 1
print(count)
