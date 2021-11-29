string_example = input('Enter string: ')

result_list = list(string_example.split(','))
result_tuple = tuple(string_example.split(','))

print("Result list is: {}".format(result_list))
print("Result tuple is: {}".format(result_tuple))
