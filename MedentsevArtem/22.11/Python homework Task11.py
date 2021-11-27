def painting():
    a = int(input('Enter a number:'))
    stars = ''
    # first triangle
    for i in range(a):
        stars += '*'
        print(stars)
    cnt = a
    # second triangle
    for i in range(a):
        cnt -= 1
        stars = ' ' * cnt + '*' * i
        print(stars)
    stars = ''
    # third triangle
    if a > 3:
        for i in range(a - 2):
            stars += '*'
            print(stars)
        for i in range(a - 3):
            print('*' * (a - 3 - i))
    else:
        for i in range(a):
            stars += '*'
            print(stars)
        for i in range(a - 1):
            print('*' * (a - 1 - i))


try:
    painting()
except(ValueError, UnboundLocalError):
    print('The given symbol is not a number')
