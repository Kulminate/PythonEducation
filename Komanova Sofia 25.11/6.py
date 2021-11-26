# 6) Написать функцию get_words(), которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)

def get_words(text):
    new_list = [',', '.', ':', '-', '–', '?', '!', '  ']
    for i in new_list:
        if i == '  ':
            text_list = text.replace(i, ' ')
        else: text_list = text.replace(i, '')
        text = text_list
    text2 =text.split(' ')
    return len(text2)


text = "dsad! sadad, - dsada sdad sda sdadas – dsad, dsadad. dsada, sda"
print(get_words(text))