star = ' * '
space = " "

#first triangle

for i in range(7):
    print(star * i)
print("")
#Second triangle

count_space = 5
count_star = 1

for i in range(6):
    print(space * count_space, star * count_star)
    count_space -= 1
    count_star += 1

#Third triangle

for i in range(5):
    print(star*i)
for i in range(3, 0, -1):
    print(star * i)




