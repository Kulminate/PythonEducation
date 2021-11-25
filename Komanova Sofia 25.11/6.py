# 6) Написать функцию get_words(), которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)
def get_words(text):
    text_list = text.split(' ')
    text_list.remove('-')
    text_list.remove('–')
    return len(text_list)


text = "dsad! sadad, - dsada sdad sda sdadas – dsad, dsadad. dsada, sda"
print(get_words(text))