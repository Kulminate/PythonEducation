#1) Написать функцию arithmetic, принимающую 3 аргумента: первые
#2 - числа, третий - операция, которая должна быть произведена над ними.
#Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(number_1: float, number_2: float, operator: str) -> str:
    if operator == "+":
        return str(number_1 + number_2)
    elif operator == "-":
        return str(number_1 - number_2)
    elif operator == "*":
        return str(number_1 * number_2)
    elif operator == "/":
        return str(number_1 / number_2)

    return "Неизвестная операция"

number_1: float = float(input("Введите первое число:").strip())
number_2: float = float(input("Введите второе число:").strip())
operation: str = input("Введите арифметическую операцию:").strip()

print(f"Результат {number_1} {operation} {number_2} равен {arithmetic(number_1, number_2, operation)}")


