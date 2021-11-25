def get_words(string):
    # a = [" ", ",", ".", "!", "?", " - ", ";", ")", "("]
    #
    # for i in a:
    #     b = string.replace(i, " ")

    new_string2 = []
    new_string = string.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(" - ", " ").replace(";", " ").replace(":", " ").replace("(", " ").replace(")", " ").split(" ")
    for elem in new_string:
        if elem != "":
            new_string2.append(elem)
    print(len(new_string2))

get_words("количество! слов в тексте. В тексте, jdj")