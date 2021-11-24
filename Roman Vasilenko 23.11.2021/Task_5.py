objects_count = 1
temp = 1
result_sum = 0
string_number = int(input('Enter string number: ' ))

for i in range(0, string_number):
    for u in range(objects_count):
        if i == range(string_number)[-1]:
            result_sum += temp
        temp += 2
    objects_count += 1

print(result_sum)