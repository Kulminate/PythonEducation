# Задание 4 Напишите проверку на то, является ли строка палиндромом
palindrom = str(input("Введите строку:"))
if palindrom == palindrom[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")