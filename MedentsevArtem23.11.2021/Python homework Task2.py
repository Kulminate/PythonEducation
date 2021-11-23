def list_and_tuple_creator(a):
    lst = []
    for i in a:
        if i.isdigit():
            lst += i
    t = tuple(lst)
    print(lst, t, sep='\n')





list_and_tuple_creator(input('Enter number range:'))
