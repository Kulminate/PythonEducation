# Написать функцию get_words(), которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)

def get_words(string: str = input('Enter string: \n')):

    line = string.split(' ')
    return print('\n words: ', len(line))
get_words()