def square(a):
    p = a * 4
    s = a * a
    d = (a ** 2) * 2
    d = d ** 0.5
    my_tuple = (p, s, d)

    return my_tuple

print(square(4))