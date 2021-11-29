a = input()
l = len(a)
b = l // 2
for i in range(l):
    if a[1-i] != a[-1-i]:

        print("It`s P")
        break
else:
    print("noop")

