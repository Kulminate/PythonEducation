def reverse_dictionary(insert_dict):
    temp_list = list(dict_items)
    result_list = []

    for i in range(len(insert_dict)):
        result_list.append((temp_list[i][1], temp_list[i][0]))

    result_dict = dict(result_list)
    return result_dict


example_dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
}
dict_items = example_dict.items()
reverse_dictionary(dict_items)

print(reverse_dictionary(dict_items))


