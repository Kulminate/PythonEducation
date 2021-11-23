def dict_reverser(d):
    l = []
    dd = {}
    for i in d:
        for j in i:
            l += [j]
            if len(l) == 2:
                dd.setdefault(l[1], l[0])
                l = []
    print(dd)





d = {1:'a', 2:'b', 3:'c'}
d_items = d.items()

dict_reverser(d_items)
