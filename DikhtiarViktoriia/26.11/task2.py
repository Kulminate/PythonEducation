from os import walk

def print_docs(directory):
    for i in walk(directory):
        print(i)

print_docs("C:/Users/dihty/PycharmProjects/PythonEducation/DikhtiarViktoriia")