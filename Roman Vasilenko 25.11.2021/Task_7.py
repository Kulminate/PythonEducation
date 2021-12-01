
for block in range(1, 10):
    print(end='\n')
    for string in range(1, 10):
        result = eval('{} * {}'.format(string, block))
        print('{} x {} = {}'.format(string, block, result), end='\t')
