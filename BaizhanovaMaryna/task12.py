a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
print("Greatest common divisor", gcd)
