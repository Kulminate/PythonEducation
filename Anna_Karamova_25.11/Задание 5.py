# Задание 5) Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе

import math

def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    end: int = int(math.sqrt(number)) + 1

    for i in range(2, end):
        if number % i == 0:
            return False

    return True


number = int(input("Введите число для проверки:"))
prime_str = "простое" if is_prime(number) else "сложное"
print(f"Число {number} {prime_str}")




