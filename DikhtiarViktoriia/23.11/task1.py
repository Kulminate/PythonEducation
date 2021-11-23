list_nums = [1, 2, 3, 4, 5, 6]
steps = int(input("Ввдите число: "))
list2 = []

for i in range(len(list_nums)):
    list2 = list_nums[-steps:] + list_nums[:-steps]
print(list2)

