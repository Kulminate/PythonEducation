# 5) Написать функцию is_prime, принимающую 1
# аргумент — число от 0 до 1000,
# и возвращающую True,
# если оно простое, и False - иначе.

def is_prime(a):
    cnt = 0
    if a == 0:
        return False
    for sub in range(1, a+1):
        if a % sub == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


correct_input = False
while not correct_input:
    integer = int(input("Введите число от 0 до 1000\n"))
    if 0 <= integer <= 1000:
        correct_input = True
    else:
        print("Некорректный ввод\n")
else:
    print(is_prime(integer))
