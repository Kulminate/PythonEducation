def numbers_matched_range(dictionary, left_range, right_range):
    result = []

    for key, value in dictionary.items():
        for index in range(left_range, right_range + 1):
            if value == index:
                result.append(key)
    return result


insert_dict = { 'a': 11,
                'b': 12,
                'c': 17,
                'd': 23,
                'e': 12
}

left_range = int(input('Enter left range: '))
right_range = int(input('Enter left range: '))
print(numbers_matched_range(insert_dict, left_range, right_range))






