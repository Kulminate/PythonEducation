def dict_range(a, b):
    d = {'a': 11, 'b':12, 'c': 17, 'd': 23, 'e':12}
    l1 = list(d.values())
    l2 = list(d)
    l3 = list()
    for i in range(a, b+1):
        if i in l1:
            l3.append(l2[l1.index(i)])
    print(l3)

try:
    dict_range(int(input('Enter first number:')), int(input('Enter second number:')))
except(ValueError, UnboundLocalError):
    print('That is not a digit. Please, rerun the algorithm.')
