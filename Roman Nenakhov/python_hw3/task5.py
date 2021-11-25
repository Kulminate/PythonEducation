# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.


def is_prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    if counter == 2:
        return True
    elif n == 0 or n == 1 or n < 0 or n > 1000:
        return 'Error'
    else:
        return False


print(is_prime(int(input())))
