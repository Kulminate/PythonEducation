def show_multiplicity_table():
    for i in range(1, 4):
        print()
        for j in range(1, 4):
            print(f"{j} x {i} = {i * j}", end="\t")


show_multiplicity_table()
