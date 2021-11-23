list_nums = [1, 2, 3, 4, 5, 6]
steps = int(input("Ввдите число: "))
list2 = []

for i in list_nums:
    list2 = list_nums[-steps:] + list_nums[:-steps]
print(list2)

#Второй вариант:

list_nums2 = [1, 2, 3, 4, 5, 6]
steps2 = int(input("Ввдите число: "))

for i in range(steps2):
    elem = list_nums2.pop(-1)
    list_nums2.insert(0, elem)
print(list_nums2)