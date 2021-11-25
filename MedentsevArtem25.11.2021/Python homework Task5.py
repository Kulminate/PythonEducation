def is_prime(a):
    b = round(a / 2)
    while b > 1:
        if a % b == 0:
            return False
        b -= 1
    return True


try:
    print(is_prime(int(input('Enter a number:'))))
except(ValueError, UnboundLocalError):
    print('Digits should be used.')
