step = int(input('Enter step : '))
example_list = list(range(11))

for i in range(step):
    temp = example_list.pop(-1)
    example_list.insert(0, temp)

print(example_list)