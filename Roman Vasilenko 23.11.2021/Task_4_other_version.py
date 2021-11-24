def numbers_matched_range(dictionary, left_range, right_range):
    result_list = []

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
left_range = 0
right_range = 13

numbers_matched_range(insert_dict, left_range, right_range)