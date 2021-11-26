example_list = ['x', 'y', 'z']
result_string = ''
index = 0

height = int(input("Enter height: "))
width = int(input("Enter width: "))


for i in range (height):
    result_string += "\n"
    for u in range(width):
        result_string += example_list[index]
        index += 1
        if index > 2:
            index = 0


print(result_string)





