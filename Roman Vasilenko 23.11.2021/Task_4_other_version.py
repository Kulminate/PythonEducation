def numbers_matched_range(dictionary, left_range, right_range):
    result_list = []

    if right_range < left_range:
        right_range, left_range = left_range, right_range

    for value in dictionary.items():
        if left_range <= value[1] <= right_range:
            result_list.append(value[0])

    return print(result_list)



insert_dict = { 'a': 11,
                'b': 12,
                'c': 17,
                'd': 23,
                'e': 12
}
left_range = int(input('Enter left range: '))
right_range = int(input('Enter left range: '))

numbers_matched_range(insert_dict, left_range, right_range)