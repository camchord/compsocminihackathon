#/usr/bin/env python

from random import randrange

class generator(object):

    def __init__(self):
        self.word_list = ['this', 'is', 'a', 'list', 'of', 'random', 'words']

    def generate_string(self, length):
        words = self.word_list
        
        rand_words = [words[randrange(0, len(words))] for _ in range(length)]
        return ' '.join(rand_words)
