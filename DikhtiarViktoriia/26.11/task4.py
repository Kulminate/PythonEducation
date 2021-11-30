def isDigit(string):
    try:
        int(string)
        print(True)
    except ValueError:
        try:
            float(string)
            print(True)
        except ValueError:
            print(False)


(isDigit("3"))
isDigit("  3  ")
isDigit("-3.23")
isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")