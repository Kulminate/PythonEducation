
for block in range(1, 4):
    print(end = '\n')
    for string in range(1, 4):
        result = eval('{} * {}'.format(string, block))
        print('{} x {} = {}'.format(string, block, result), end='\t')
