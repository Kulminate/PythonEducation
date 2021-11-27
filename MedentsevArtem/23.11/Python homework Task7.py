def swapnumbers():
    x = 5
    y = 3
    x *= y
    y = x / y
    x /= y
    print('x is ', round(x), ';', ' y is ', round(y), sep='')


swapnumbers()
