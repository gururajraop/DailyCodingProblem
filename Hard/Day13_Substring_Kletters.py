"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

import os
import sys
import numpy as np


def find_longest_substring(s, k=2):
    pass


if __name__ == '__main__':
    assert find_longest_substring("abcba", k=2) == "bcb", "Test1 Failed"
    assert find_longest_substring("abcba", k=3) == "abcba", "Test2 Failed"
    assert find_longest_substring("kskellrlrk", k=2) == "llrlr", "Test3 Failed"