# 6) Написать функцию get_words(),
# которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)

def get_words(text):
    text.replace("-", "")
    word_count = len(text.split(" "))
    return word_count


text = input("Ведите текст\n")
print(get_words(text))
