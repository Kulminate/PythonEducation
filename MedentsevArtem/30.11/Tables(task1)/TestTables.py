from Tables import Table, RoundTables, RectangleTables

if __name__ == '__main__':

    a = RoundTables(2)
    print(a.square_finder())

    a = RectangleTables(4, 4)
    print(a.square_finder())

    a = Table(4)
    print(a.square_finder())
