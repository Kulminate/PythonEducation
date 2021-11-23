# Выполнить циклический сдвиг в списке целых чисел на указанное число шагов.
# Сдвиг также должен быть кольцевым, то есть элемент, вышедший за пределы списка,
# должен появляться с другого его конца.

steps = int(input("Пожалуйста, введите шаг: "))
list_of_numbers = input("Пожалуйста введите нужное количество чисел через пробел: ")

numbers = [int(i) for i in (list_of_numbers.split(' '))]

print("Ваш список чисел: ", numbers)

if steps < 0:
    steps = abs(steps)
    for i in range(steps):
        numbers.append(numbers.pop(0))
else:
    for i in range(steps):
        numbers.insert(0, numbers.pop())

print("Измененный список чисел: ", numbers)
