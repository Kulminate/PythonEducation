# Задание 6 Вывести print() следующего вида, он состоит из строки xyz, но строка не начинается с начала,
# если она не закончилась на предыдущей строке:

#Необходимо использовать цикл в цикле

#xyzxy
#zxyzx
#yzxyz
#xyzxy

#Длина этого массива должна определяться переменной l, высота переменной h
string_1 = 'xyz'
l = 5
h = 4
count = 0

for i in range(h):
    print()
    for j in range(l):
       print(string_1[count], end='')
       count += 1
       if count > 2:
            count = 0

