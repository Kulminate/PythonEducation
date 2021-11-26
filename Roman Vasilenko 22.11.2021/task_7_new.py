first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print('''Numbers successfully changed. 
        First number equal: {}
        Second number equal: {} '''.format(first_number, second_number))
