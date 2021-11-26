# дз:

# 1) Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть;
# * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic (a, b, c):
	if c == "+" :
		return (a + b)
	elif c == "-":
		return (a - b)
	elif c == "*":
		return (a * b)
	elif c == "/":
		return (a / b)
	else :
		return ("Unknown operation")
print (arithmetic(5, 8, '+'))
print (arithmetic(4, 13, '*'))
print (arithmetic(34, 12, '-'))
print (arithmetic(200, 10, '/'))
print (arithmetic(0, 0, 0))