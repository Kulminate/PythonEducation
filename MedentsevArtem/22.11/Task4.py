def palindrome():
    a = input('Enter a string to check if it is a palindrome:')
    b = 0
    half_size = round(len(a)/2)
    for i in range(half_size):
        rev = i * (-1) - 1
        if a[i] != a[rev]:
            print('this string is not a palindrome')
            b += 1
            break
    if b == 0:
        print('this string is a palindrome')


palindrome()
