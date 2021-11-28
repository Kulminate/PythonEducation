# Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.
import os


def print_docs(directory: str = '.'):

    directory_list = []
    for item in os.walk(directory):
        directory_list.append(item)

    if len(directory_list) == 0:
        raise Exception('Directory not found')

    for current, folders, items in directory_list:
        print(f'{current}\\\n Items in {current}:  {items}')



directory = input('Enter way to directory or directory name on current folder: ')
print_docs(directory)
