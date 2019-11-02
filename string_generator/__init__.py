#/usr/bin/env python

from random import randrange
from pathlib import Path

DICTIONARY = 'dictionary.txt'

def get_dictionary_path(dictionary=None):

    if dictionary is None:
        path = Path(__file__).parent.absolute()
        path = path / DICTIONARY
    else:
        path = Path(dictionary)

    return path

def load_words(filepath):
    
    with open(filepath, 'r') as dictionary:
        word_list = [word.strip() for word in dictionary]

    return word_list

class generator(object):

    def __init__(self, words=None):
        if words is None:
            self.word_list = load_words(get_dictionary_path())
        else:
            self.word_list = words

    def generate_string(self, length):
        words = self.word_list
        
        rand_words = [words[randrange(0, len(words))] for _ in range(length)]
        return ' '.join(rand_words)
