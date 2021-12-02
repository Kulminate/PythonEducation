string = input("Введите строку: ")
if string.lower() == string[::-1].lower():
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")