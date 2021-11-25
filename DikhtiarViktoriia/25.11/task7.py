a = 0
for i in range(1, 4):
    print(end="\n")
    for j in range(1, 4):
        a = i * j
        print('{} * {} = {}'.format(j, i, a), end="\t")