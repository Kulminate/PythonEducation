from Table import Table, RectTable, RoundTable

if __name__ == '__main__':

    table = Table()
    print(table.number_legs)
    # print(table.square())

    rect_table = RectTable(length=5, width=5)
    print(rect_table.number_legs)
    rect_table.square()

    round_table = RoundTable(5)
    round_table.square()

