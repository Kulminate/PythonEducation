# 2) Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов при
# помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить
# при помощи функции walk() модуля os.
from os import walk


def print_docs(directory):
    for i in walk(directory):
        print(i)


print(print_docs("D:\directory1"))

# "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe" C:/Users/Maks/PycharmProjects/PythonEducation/MSkuba261121/Task2.py
# ('D:\\directory1', ['Folder1', 'Folder2'], [])
# ('D:\\directory1\\Folder1', [], ['firs.txt'])
# ('D:\\directory1\\Folder2', [], ['Second.txt', 'third.txt'])
# None
