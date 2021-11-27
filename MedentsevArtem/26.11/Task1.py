def read_lines(lines, file):
    d = {}
    lst = []
    cnt = 1
    with open(file, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            d.setdefault(cnt, i)
            cnt += 1
    for i in range(lines):
        cnt -= lines
        lst += [d[cnt]]
        cnt += 1
    return lst


print(*read_lines(3, 'article.txt'), sep='')