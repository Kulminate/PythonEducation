# Написать функцию get_words(), которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)

def get_words(string: str = input('Enter string: \n')):

    temp_list = string.split(' ')
    # return print(temp_list)
    return print('\n Count of worlds in enter string is: ', len(temp_list))


get_words()