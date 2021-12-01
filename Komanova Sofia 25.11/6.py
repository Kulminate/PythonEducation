# 6) Написать функцию get_words(), которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)

def get_words(text):
    new_list = [',', '.', ':', '-', '–', '?', '!', '  ']
    for i in new_list:
        if i == '  ':
            text_list = text.replace(i, ' ')
        else: text_list = text.replace(i, ' ')
        text = text_list
    list_text2 =text.split(' ')
    just_word = list()
    for j in list_text2:
        if j != '':
            just_word.append(j)
    return len(just_word)


text = "dsad! sadad, - dsada sdad sda sdadas – dsad, dsa.dad. dsada, sda"
print(get_words(text))