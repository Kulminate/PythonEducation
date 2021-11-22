input_number = input("Enter number: ")
sum_number = 0

for number in input_number:
    sum_number += int(number)

print("The sum of the digits of the number is: {}".format(sum_number))