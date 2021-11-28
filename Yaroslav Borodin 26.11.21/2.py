# 2) Выберите любую папку на своем компьютере, имеющую вложенные директории.
# Выведите на печать в терминал ее содержимое,
# как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной
# директории можно осуществить при помощи функции walk() модуля os.
import os


def print_docs(dir):
    for dir_tuple in os.walk(dir):
        for file_name in dir_tuple[2]:
            with open(dir_tuple[0]+"\\"+file_name, "r") as file:
                print(f"\n\n{file_name}\n")
                file_lines = file.readlines()
                for line in file_lines:
                    print(line)


directory = input("Введите путь к папке\n")
print_docs(directory)
