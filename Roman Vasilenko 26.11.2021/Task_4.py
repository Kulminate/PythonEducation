# Написать метод isDigit, который возращает указанная строка число или нет.

def isDigit(enter_string: str = input('Enter string: ')):
    try:
        if int(enter_string):
            return 'Yes'

    except:
        try:
            if float(enter_string):
                return 'Yes'
        except:
            return 'No'


print(isDigit())


