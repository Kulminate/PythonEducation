# Задание 6) Написать функцию get_words(), которая подсчитывает количество слов в тексте.
# (В тексте может быть несколько предложений со знаками пунктуации)
import string


def get_words(text: str) -> int:
    numberOfWords: int = 0

    for s in text.split():
        if s.strip(string.punctuation).isalpha():
            numberOfWords += 1

    return numberOfWords


text = "Lorem ipsum dolorem sit amet"

print(f"Текст {text} состоит из {get_words(text)} слов")
