def cyclical_shift(myrange):
    a = [1, 2, 3, 4, 5]
    for i in range(myrange):
        temporary = a.pop()
        a.insert(0, temporary)
    print(a)



try:
    cyclical_shift(int(input('Enter a digit:')))
except(ValueError, UnboundLocalError):
    print('That is not a digit. Please, rerun the algorithm.')