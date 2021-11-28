# Написать метод isDigit, который возращает указанная строка число или нет.


def isDigit(line):
    try:
        float(line)
        return True
    except ValueError:
        return False


# True
print(isDigit("3"))
print(isDigit("  3  "))
print(isDigit("-3.23"))
# False
print(isDigit("3-4"))
print(isDigit("  3   5"))
print(isDigit("3 5"))
print(isDigit("zero"))
