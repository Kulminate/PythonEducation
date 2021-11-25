def arithmetic(number_one: int = input('first num \n'), number_two: int = input('second num \n'), operation: str = input('operation \n')):

    try:
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':

            result = eval('{} {} {}'.format(number_one, operation, number_two))
            return print('{} {} {} = {}'.format(number_one, operation, number_two, result))

        else: return print('Operation symbol incorrect.')

    except ZeroDivisionError:
        print('ZeroDivisionError')


arithmetic()
