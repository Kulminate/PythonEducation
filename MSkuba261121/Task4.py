#4) Написать метод isDigit, который возращает указанная строка число или нет.

# Примеры, в которых метод должен возвращать true
# isDigit("3")
# isDigit("  3  ")
# isDigit("-3.23")
#
# Примеры, в которых метод должен возвращать false
# isDigit("3-4")
# isDigit("  3   5")
# isDigit("3 5")
# isDigit("zero")
# Вызовы методов с указанными как позитивными так и негативными случаями сразу
# прописываем что бы мне было удобнее проверять

def isDigit(s):

    try:
        int(s)
        print(True)
    except ValueError:
        try:
            float(s)
            print(True)
        except ValueError:
            return (False)


isDigit("3")
isDigit("  3  ")
isDigit("-3.23")
isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")