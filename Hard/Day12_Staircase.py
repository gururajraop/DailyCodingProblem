"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

import os
import sys
import numpy as np


def get_unique_ways(n, steps):
    pass


if __name__ == '__main__':
    assert get_unique_ways(4, [1, 2]) == 5, 'Fail: Test 1 failed'
    assert get_unique_ways(5, [1, 3]) == 4, 'Fail: Test 2 failed'

    n = int(input("Enter the number of steps\n"))
    steps = input("Enter a list of steps that can be climbed, separated by space\n").split()
    steps = np.asarray(steps, dtype=np.int)

    result = get_unique_ways(n, steps)
    print("Number of ways to climb {} steps being able to climb {} steps at a time is: {}".format(n, steps, len(result)))
    print("The unique ways are: ", result)
