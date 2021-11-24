q = input("Enter first number: ")
w = input("Enter second number: ")

integer_part = int(q) // int(w)
remainder_part = int(q) % int(w)

print("The integer part after division is: {}".format(integer_part))
print("Remainder of division is: {}".format(remainder_part))