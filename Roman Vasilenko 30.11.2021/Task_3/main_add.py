from ADD import Distance

distance_1 = Distance(1000, 'meters')
distance_2 = Distance(1000, 'kilometers')
# distance_3 = Distance(1000, 'сentimeters')

print(distance_1, distance_2)

sum_kilometers = distance_2 + distance_1
print(sum_kilometers)
sum_meters = distance_1 + distance_2
print(sum_meters)


