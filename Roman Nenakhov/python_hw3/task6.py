 # Написать функцию get_words(), которая подсчитывает количество слов в тексте.
 # (В тексте может быть несколько предложений со знаками пунктуации)


def get_words(text):
    x = text.split(" ")
    y = [i for i in x if i != "-"]
    return len(y)


print(get_words(input()))
