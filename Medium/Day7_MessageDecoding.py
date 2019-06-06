"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import os
import sys
import numpy as np


def decode_count(message):
    if len(message) <= 1:
        return 1        # Even empty string can be decoded as empty message.

    count = np.zeros(len(message))
    for i in reversed(range(len(message))):
        if message[i].startswith('0'):
            count[i] = 0
        elif i == len(message) - 1:
            count[i] = 1
        elif i == len(message) - 2:
            if int(message[i] + message[i + 1]) <= 26:
                count[i] = 1 + count[i + 1]
            else:
                count[i] = 1
        else:
            if int(message[i] + message[i + 1]) <= 26:
                count[i] = count[i + 2]
            count[i] += count[i + 1]

    return count[0]


if __name__ == '__main__':
    assert decode_count('111') == 3, "Fail: Test 1 of input message 111"
    assert decode_count('621182118110') == 25, "Fail: Test 1 of input message 621182118110"

    message = input("Please enter the coded message: ")
    print("Number of ways to decode the given message is: ", decode_count(message))