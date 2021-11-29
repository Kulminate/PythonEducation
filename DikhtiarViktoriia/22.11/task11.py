a1 = "*"
i1 = 0
c1 = ""
while(i1 < 6):
    c1 += a1
    print(c1)
    i1 += 1


n = 7
for i in range(n + 1):
    num = n - i
    print(" " * num + "* " * i)


a2 = 1
for i in range(4):
    print("*" * a2)
    a2 += 1
a2 = 3
for i in range(3):
    print("*" * a2)
    a2 -= 1