# 5) Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
def is_prime(num):
    if num in range(1001):
        new_list = list()
        n = num
        if num == 0:
            return False
        while n != 0:
            if num%n == 0:
                new_list.append(n)
            n-=1
        if len(new_list)>2:
            return False
        else: return True

    else: print("число не входит в диапазон от 0 о 1000")

print(is_prime(1000))