# 4) Написать метод isDigit, который возращает: указанная строка число или нет.

# Примеры, в которых метод должен возвращать true
# isDigit("3")
# isDigit("  3  ")
# isDigit("-3.23")
# Примеры, в которых метод должен возвращать false
# isDigit("3-4")
# isDigit("  3   5")
# isDigit("3 5")
# isDigit("zero")
# Вызовы методов с указанными как позитивными так и негативными случаями сразу прописываем,  чтобы мне было
# удобнее проверять

def isDigit(the_string):
    try:
        float(the_string)
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