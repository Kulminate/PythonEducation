# 4) Написать метод isDigit, который возращает указанная строка число или нет.
def isDigit(line):
    try:
        float(line)
        return f"Указанная строка \"{line}\" является числом"
    except ValueError:
        return f"Указанная строка \"{line}\" не является числом"

print(isDigit('2sd4323sds'))
print(isDigit('2'))
print(isDigit('-2'))
print(isDigit('0.4322'))
