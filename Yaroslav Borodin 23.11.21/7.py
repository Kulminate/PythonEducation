def reverse_variables(a, b):
    a += b
    b -= a
    b = -b
    a -= b
    return a, b


a = int(input("Введите переменную a\n"))
b = int(input("Введите переменную b\n"))
res = reverse_variables(a, b)
print(f"before reverse: a = {a}  b = {b}")
print(f"reversed: a = {res[0]}  b = {res[1]}")
