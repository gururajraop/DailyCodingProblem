"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

import os
import sys
import numpy as np


def find_longest_substring(s, k=2):
    if k == 0:
        return ""
    elif k == 1:
        return s[0]
    else:
        substring = ""              # Current substring with max k distinct chars
        longest_substr = ""         # The longest substring so far with max k distinct chars
        chars = []                  # Distinct chars in the substring
        for i, c in enumerate(s):
            if c in chars:          # The character is already seen in the substring
                substring = substring + c
            else:                   # New character to the substring
                if len(chars) >= k: # The substring already had k distinct characters
                    # Remove the character that occur farthest to the current character
                    last_char = substring[-1]
                    remove_char = chars[0] if last_char == chars[1] else chars[1]
                    # Obtain the last position of that character
                    positions = [pos for pos, char in enumerate(substring) if char == remove_char]
                    last_occ = max(positions)
                    # Remove the character
                    substring = substring[last_occ+1:]
                    chars.remove(remove_char)
                # Add the character to the substring
                substring = substring + c
                chars.append(c)
            # Replace the longest substring with the substring if substring is longer
            if len(substring) > len(longest_substr):
                longest_substr = substring

        print("Given string: {}\t\tk: {}\t longest substring: {}".format(s, k, longest_substr))
        return longest_substr



if __name__ == '__main__':
    assert find_longest_substring("abcba", k=2) == "bcb", "Test1 Failed"
    assert find_longest_substring("abcba", k=3) == "abcba", "Test2 Failed"
    assert find_longest_substring("kskellrlrk", k=2) == "llrlr", "Test3 Failed"