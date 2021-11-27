def square(a):
    return a * 4, a * a, (2*(a**2))**0.5


try:
    print(square(int(input('Enter the square side:'))))
except(ValueError, UnboundLocalError):
    print('A digit should be used.')
