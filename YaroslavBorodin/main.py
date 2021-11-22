mystring="Hello World!"
first=mystring[0]
last=mystring[-1]
print(f"\n Complete string: \"{mystring}\", first element: \"{first}\", last element: \"{last}\" \n")

first_num_string = "6"
second_num_string = "7"
print("\n Sum of two numbers: first_num + second_num = ", int(first_num_string)+int(second_num_string),"\n")

num = int(input("Enter some number "))
print("Your number: {}".format(num))
print("Your number squared: {}\n".format(num**2))

some_string = input("Enter some string: ")
if(some_string==some_string[::-1]):
    print("This string is palindrome")
else:
    print("This string isnt palindrome")

a = 6
b = "s"
print(f"\na = {a}, b = {b}")
buf = a
a = b
b = buf
print(f"Exchange of values: a = {a}, b = {b}")




