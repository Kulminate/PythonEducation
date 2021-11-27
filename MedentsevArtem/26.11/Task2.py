# 2) Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов
# при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить
# при помощи функции walk() модуля os.
from os import walk


def print_docs(directory):
    return [i for i in walk(directory)]


print(*print_docs('C:/Program Files/Internet Explorer'), sep='\n')
