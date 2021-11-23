first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

divide_list = []

if first_number > second_number:
    lower_number = second_number
else: lower_number = first_number

for i in range(1, lower_number+1):
    if first_number % i == 0 and second_number % i == 0:
        divide_list.append(i)

divide_list.sort()

print(divide_list[-1])