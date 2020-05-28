"""
read file
create a string from read file
clear special characters, punctuation signs, new lines,
create a list of words from string
create a dictionary from list
compare 2 dictionaris
"""

import string


def read_text(filename):

    in_file = open(filename, 'r')
    line = in_file.read()
    return line


# print(read_text('sonnet_18'))
line = read_text('sonnet_18')


def find_words(text):
    text = text.replace('\n', ' ')
    text = text.replace("â€™", "'")

    for char in string.punctuation:
        text = text.replace(char, '')
    words = text.split(' ')

    return words


def frequencies(words):

    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


def calculate_similarity(dict_1, dict_2):

    diff = 0
    total = 0

    for word in dict_1.keys():
        if word in dict_2.keys():
            diff += abs(dict_1[word] - dict_2[word])
        else:
            diff += dict_1[word]

    for word in dict_2.keys():
        if word not in dict_1.keys():
            diff += dict_2[word]

    total = sum(dict_1.values()) + sum(dict_2.values())
    difference = diff / total
    similar = 1.0 - difference
    return round(similar, 2)


text_1 = read_text('sonnet_18')
text_2 = read_text('sonnet_19')

words_1 = find_words(text_1)
words_2 = find_words(text_2)

dictionary_1 = frequencies(words_1)
dictionary_2 = frequencies(words_2)

final_score = calculate_similarity(dictionary_1, dictionary_2)
print(final_score)
