def get_words(text):
    start_word = False
    word_cnt = 0
    for symbol in text:
        if not symbol.isalpha():
            if start_word:
                start_word = False
            continue
        else:
            if not start_word:
                word_cnt += 1
            start_word = True
    return word_cnt


text = input("Ведите текст\n")
print(get_words(text))
