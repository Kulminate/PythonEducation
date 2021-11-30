# Вывести print() следующую вид, он состоит из строки xyz, но строка не начинается с начале,
# если она не закончилась на предыдущей строке:
# Необходимо использовать цикл в цикле
# xyzxy
# zxyzx
# yzxyz
# xyzxy
# Длина должна этого массива определяться переменной l, высота переменной h

my_list = ["x", "y", "z"]
result = ""
count = 0

l = int(input("Введите длину массива: "))
h = int(input("Введите высоту массива: "))

for i in range(h):
    result += "\n"
    for u in range(l):
        result += my_list[count]
        count += 1
        if count > 2:
            count = 0

print(result)
