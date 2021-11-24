string = "xyz"
l = 5
h = 5
index = 0

for i in range(h):
    print()
    for j in range(l):
        print(string[index], end="")
        index += 1
        if index > 2:
            index = 0