# Задание 2) Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.

import os
dir = "task2_folder"

def print_docs(directory):

    for dir_path, _, files in os.walk(directory):
        print(dir_path)
        for file_name in files:
            print(f"\t{file_name}")

print_docs(dir)
