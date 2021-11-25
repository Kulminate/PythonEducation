input_string = input("Введите последовательность чисел, разделённых запятой\n")
print(input_string)
int_list = input_string.split(",")
int_tuple = tuple(int_list)
print(int_list)
print(int_tuple)

