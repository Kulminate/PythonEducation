#Задание 11 Нарисовать треугольник заданной размерности.


print("==============")
n = 7
for i in range(n+1):
    k = n-1
    print(" " * k + "* " * i)

print("==============")
a2 = 1
for i in range(4):
    print("*" * a2)
    a2 += 1
a2 = 3
for i in range(3):
    print("*" * a2)
    a2 -=1

print("==============")

n = 7
for i in range (n+1):
    num = n- 1
    print(" " * num + "*" * i )



