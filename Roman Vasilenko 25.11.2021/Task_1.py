def arithmetic(number_one: int = input('first num \n'), number_two: int = input('second num \n'), operation: str = input('operation \n')):

    try:
        result = eval('{} {} {}'.format(number_one, operation, number_two))
        return print('{} {} {} = {}'.format(number_one, operation, number_two, result))

    except ZeroDivisionError:
        print('ZeroDivisionError')
    except NameError:
        print('Enter valid numbers or operation symbol')
    except SyntaxError:
        print('Enter valid numbers or operation symbol')


arithmetic()
