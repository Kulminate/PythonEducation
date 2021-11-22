def check_palindrom(input_str):
    if input_str == input_str[::-1]:
        return print("It's palindrom")
    else:
        return print('Not palindrome')


input_str = input('Enter string: ')
print(check_palindrom(input_str))
