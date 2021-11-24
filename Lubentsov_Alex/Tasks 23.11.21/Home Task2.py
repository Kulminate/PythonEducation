#task 4

dict =  { 'a': 11, 'b ':12, 'c': 17, 'd': 23, 'e':12 }
def func_reversed(dict, x, y):
        return [dict_item[0] for dict_item in dict.items() if x <= dict_item[1] <= y]
    print(func_reversed(dict, 12, 30))



# task 2
numbers = input('Введите числа разделенные запятой: ')
numbers_splitting = numbers.split(',')
num = map(int, numbers_splitting)
list1 = list(num)
tuple1 = tuple(list1)
print(list1)
print(tuple1)

# task 7
a = 17
b = 18
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# task 1
def sdvig(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers)

sdvig(numbers, -3)
print(numbers)



# task 3
def reversed_dict(insert_dict):
    temp_list = list(dict_items)
    result_list = []

    for i in range(len(insert_dict)):
        result_list.append((temp_list[i][1], temp_list[i][0]))

    result_dict = dict(result_list)
    return result_dict


my_dict = { 43: 'dsf', 32: 'gdffg', 34254: 'fgdfh', 3223: 'ghdgg', 667: 'hfhkl'}
dict_items = my_dict.items()
reversed_dict(dict_items)

print(reversed_dict(dict_items))


# task 5
list_xyz = ["x", "y", "z"]
result = ""
count = 0

l = int(input("Введите длину массива: "))
h = int(input("Введите высоту массива: "))

for i in range(h):
    result += "\n"
    for u in range(l):
        result += list_xyz[count]
        count += 1
        if count > 2:
            count = 0

print(result)




# task 6
ln = int(input('Введите № строки: '))
current_number = 1
stop = 2
result = list()

for i in range(0, ln):
    result = list()
    for column in range(1, stop):
        print(current_number, end=' ')
        result.append(current_number)
        current_number += 2
    print(" ")
    stop += 1

print(sum(result))


