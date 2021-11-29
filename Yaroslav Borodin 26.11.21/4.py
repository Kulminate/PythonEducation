def isDigit(num_str):
    num_started = False
    num_detected = False
    point_detected = False
    for s in num_str:

        if num_started and s == " ":
            num_started = False
            num_detected = True

        if num_started and (s == "-" or (s == "." and point_detected)):
            return False

        if s == ".":
            point_detected = True

        if s == " ":
            continue

        if s.isalpha() or (num_detected and s != " "):
            return False

        if s.isnumeric() or s == "-" and not num_detected:
            num_started = True

    return True


positive_test_set = ["3", "  3  ", "-3.23"]
negative_test_set = ["3-4", "  3   5", "zero"]

for item in positive_test_set:
    print(item)
    print(isDigit(item))

for item in negative_test_set:
    print(item)
    print(isDigit(item))
