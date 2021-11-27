import re


def get_words(string):
    result = len(re.findall('\w+', string))
    print(result)


print(get_words(input('Enter a text:')))