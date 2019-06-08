"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

import os
import sys
import numpy as np

from collections import defaultdict


class Vocabulary:
    def __init__(self):
        self.vocab = defaultdict(lambda: defaultdict(list))

    def add_item(self, str_set):
        for item in str_set:
            self.vocab[item[0]][item[1]].append(item)

    def get_items(self, search_term):
        return self.vocab[search_term[0]][search_term[1]]


if __name__ == '__main__':
    print("Autocomplete System")
    Vocab = Vocabulary()
    input_strings = ['dog', 'deer', 'deal']
    Vocab.add_item(input_strings)
    search_term = "de"
    print("Result of autocomplete system: {}".format(Vocab.get_items(search_term)))
    
