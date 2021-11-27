def dict_reverser():
    d_items = primary_dict_setup()
    main_feature(d_items)


def primary_dict_setup():
    d = {1:'a', 2:'b', 3:'c'}
    return d.items()


def main_feature(d):
    l = []
    dd = {}
    for i in d:
        for j in i:
            l += [j]
            if len(l) == 2:
                dd.setdefault(l[1], l[0])
                l = []
    print(dd)


dict_reverser()
