first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

while second_number != 0:
        (first_number, second_number) = (second_number, first_number % second_number)

print("GCD of entered numbers is : {}".format(first_number))
