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

a = True
b = "71"
print(f"\na = {a}, b = {b}")
a, b = b, a
print(f"Exchange of values: a = {a}, b = {b}")

q = 56
w = 9
print(f"\nq = {q}, w = {w}\nq/w = {q / w}")

some_int = 695
sum = 0
for n in str(some_int):
    sum+=int(n)
print(f"\nSum of digits of an integer {some_int} is {sum}")

newstring = "Hello beautiful World!"
your_char = input("\nEnter some character ")
print(newstring.count(your_char))

for n in range(1, 7):
    print("*" * n)


for n in range(1, 7):
    print(f'{" " * (6-n)}{"*"*n}')

for n in range(1, 8):
    if (n < 4):
        print("*" * n)
    else:
        print("*" * (8-n))
