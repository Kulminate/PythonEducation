# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
# и False - иначе.

def is_prime(num=int(input('Enter number: '))):

    if 0 <= num <= 1000:

        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return 'Number must be between 0 and 1000 \n'


print(is_prime())

# Cycle which print all prime numbers in range (1, 100)

# for i in range(1, 100):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
