example_list = ['x', 'y', 'z']
result_string = ''
index = 0


for i in range (4):
    result_string += "\n"
    for u in range(4):
        result_string += example_list[index]
        index += 1
        if index > 2:
            index = 0


print(result_string)
