def read_last(lines, file):
    try:
        with open(file, "r", encoding="utf8") as file:
            content = file.read().splitlines()
            if lines >= 0 and lines <= len(content):
                print(content[-lines:])
            else:
                print("Введено отрицательное число или число больше количества строк")
    except IOError as e:
        print(e)
read_last(2, "article.txt")
read_last(2, "articl.txt")
read_last(-1, "article.txt")
read_last(9, "article.txt")
