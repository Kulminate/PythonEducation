my_dict = {1: "one", 2: "two", 3: "three"}
items_dict = my_dict.items()
new_dict = {}

def dict_reverse(a):
    for i in a:
        new_dict.setdefault(i[1], i[0])
    print(new_dict)

dict_reverse(items_dict)