def NOD(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    print(a)


try:
    NOD(int(input('type the first number:')), int(input('type the second number:')))
except(ValueError, UnboundLocalError):
    print('That is not a digit.')
