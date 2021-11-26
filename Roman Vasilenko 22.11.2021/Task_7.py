first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

first_number, second_number = second_number, first_number

print('''Numbers successfully changed. 
        First number equal: {}
        Second number equal: {} '''.format(first_number, second_number))