num_str = int(input("Введите номер строки: "))

string = 1
num = 1
sum_nums = 0

for i in range(num_str):
    for j in range(string):
        if string == num_str:
            sum_nums += num
        num += 2
    string += 1
print(sum_nums)
