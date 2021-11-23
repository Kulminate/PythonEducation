def cyclical_shift(l, h):
    a = 'xyz'
    cnt = 0
    for i in range(h):
        for i in range(l - 1):
            print(a[cnt], end='')
            if cnt > 1:
                cnt -= 2
            else:
                cnt += 1
        print(a[cnt])
        if cnt > 1:
            cnt -= 2
        else:
            cnt += 1


try:
    cyclical_shift(int(input('Enter a digit length:')), int(input('Enter a digit hight')))
except(ValueError, UnboundLocalError):
    print('That is not a digit.')