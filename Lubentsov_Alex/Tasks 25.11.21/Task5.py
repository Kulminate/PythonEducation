# 5) Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(number=int(input('Enter number: '))):

    if 0 <= number <= 1000:
        if number == 0:
            return "Its null"
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return 'Number must be from 0 to 1000 \n'

print(is_prime())