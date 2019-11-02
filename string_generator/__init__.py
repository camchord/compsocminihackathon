#/usr/bin/env python

from random import randrange

DICTIONARY = 'dictionary.txt'

def load_words(filename):
    
    with open(filename, 'r') as dictionary:
        word_list = [word.strip() for word in dictionary]

    return word_list

class generator(object):

    def __init__(self, words=None):
        if words is None:
            self.word_list = load_words(DICTIONARY)
        else:
            self.word_list = words

    def generate_string(self, length):
        words = self.word_list
        
        rand_words = [words[randrange(0, len(words))] for _ in range(length)]
        return ' '.join(rand_words)
