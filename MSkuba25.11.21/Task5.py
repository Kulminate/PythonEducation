# 5) Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
def is_prime(numb=int(input("input numb 0 to 1000"))):

    if numb >= 1:
        return "true"
    elif numb % 1:
        return "true"
    elif numb % numb:
        return "true"
    else:
        return "false"
print(is_prime())
