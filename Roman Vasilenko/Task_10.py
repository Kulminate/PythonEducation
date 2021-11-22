# How many times each character occurs in a string

# enter_string = input("Enter string: ")
#
# for symbol in enter_string:
#     counter = 0
#     for i in range(len(enter_string)):
#         if symbol == enter_string[i]:
#             counter += 1
#     print('Symbol "{}" appears in the string {} times '.format(symbol, counter))

#How many times a specific character occurs in a string

enter_string = input("Enter string: ")
counter = enter_string.count(input("Enter symbol: "))
print("Entered character occurs in a string {} times".format(counter))
