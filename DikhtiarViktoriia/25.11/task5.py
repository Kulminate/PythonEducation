def is_prime(num):
    if num >= 1 and num <= 1000:
        for i in range(2, num):
            if num % i == 0:
                return True
            else:
                return False
    else:
        return "Число больше 1000 или меньше 1"

print(is_prime(int(input("Введите число от 1 до 1000: "))))