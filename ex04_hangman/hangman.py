import json
from random import randrange
from copy import copy


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def find_char_indexes(char, word):
    word_arr = list(copy(word))
    indexes = list()
    while char in word_arr:
        chr_index = str().join(word_arr).find(user_chr)
        word_arr.pop(chr_index)
        indexes.append(chr_index)
    return indexes


def replace_by_index(index, char, word):
    word = list(word)
    word[index] = char
    return str().join(word)


WORDS = read_json('words.json')


word_to_found = WORDS[randrange(len(WORDS))]
attemps_left = chr_count = len(word_to_found)
user_word = '_' * chr_count
chars_found = list()

while '_' in user_word and attemps_left > 0:
    print(f'Word to found: {word_to_found}')
    print(f'\nWORD : {user_word}\n')
    print(f'Attempts left : {attemps_left}')
    user_chr = input('Type a letter : ')

    if user_chr in word_to_found:
        if user_chr in chars_found:
            print(f'{user_chr} already found')
            continue
        indexes = find_char_indexes(user_chr, word_to_found)
        for i in indexes:
            user_word = replace_by_index(i, user_chr, user_word)
        print(f'{user_chr} is in word: {user_word}')
    else:
        print(f'{user_chr} not in word ')

    attemps_left -= 1

if '_' in user_word:
    print('You lost')
else:
    print('You win')
