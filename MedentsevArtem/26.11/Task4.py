# 4) Написать метод isDigit, который возращает указанная строка число или нет.
def isDigit(a):
    try:
        int(a)
        return True
    except ValueError:
        try:
            float(a)
            return True
        except ValueError:
            return False


# Примеры, в которых метод должен возвращать true
print(isDigit("3"))
print(isDigit("  3  "))
print(isDigit("-3.23"))

# Примеры, в которых метод должен возвращать false
print(isDigit("3-4"))
print(isDigit("  3   5"))
print(isDigit("3 5"))
print(isDigit("zero"))
