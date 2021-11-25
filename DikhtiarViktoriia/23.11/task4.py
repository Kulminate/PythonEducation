my_dict = {'a': 11, 'b': 12, 'c': 17, 'd': 23, 'e': 12}
x = 12
y = 20

def get_items(d):
    for i in d:
        if d.setdefault(i) >= x and d.setdefault(i) <= y:
            print(i)

get_items(my_dict)