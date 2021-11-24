def list_and_tuple_creator(a):
    digit = 0
    lst = []
    cnt = 0
    for i in a:
        if i.isdigit():
            digit *= 10
            digit += int(i)
            cnt += 1
        else:
            if cnt > 0:
                lst.append(digit)
                cnt = 0
                digit = 0
    if cnt != 0:
        lst.append(digit)
    t = tuple(lst)
    print(lst, t, sep='\n')





list_and_tuple_creator(input('Enter number range:'))
