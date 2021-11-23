# create function, which return summ of 2 input numbers
def sum_numbers(str1, str2):
    return eval(str1 + '+' + str2)


str1 = input('Enter first number: ')
str2 = input('Enter second number: ')

print(sum_numbers(str1, str2))
