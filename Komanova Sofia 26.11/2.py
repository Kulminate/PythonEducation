# 2) Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.
import os

def print_docs(directory):
    tree = os.walk(directory)
    for d in tree:
        print("Содержимое директории:",d)
        for i in d:
            print("Содержимое подкаталога:", i)




print_docs("/Users/sofiakomanova/Movies")