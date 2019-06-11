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


def get_unique_ways1(n):
    assert n > 0, "Invalid input! non-positive input"

    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1], [2]]
    else:
        a, b = [[1]], [[1, 1], [2]]
        for _ in range(n-2):
            new_a = [l + [2] for l in a]
            new_b = [l + [1] for l in b]
            a, b = b, new_a + new_b

        return b


def get_unique_ways2(n, steps):
    steps = np.array(steps)
    assert (n > 0) and (steps > 0).all(), "Invalid input! non-positive input"
    assert len(steps) > 0, "Not all jumps can be bigger than the total number of steps"

    cache = [[] for _ in range(n+1)]
    for i in range(n+1):
        if i < steps[0]:
            continue
        for s in steps:
            if i == s:
                cache[i].append([s])
            elif i > s:
                item = [l + [s] for l in cache[i-s]]
                cache[i] = cache[i] + item
            else:
                break

    return cache[n]


if __name__ == '__main__':
    # With steps = {1, 2}
    assert len(get_unique_ways1(1)) == 1, 'Fail: Test 1 failed'
    assert len(get_unique_ways1(2)) == 2, 'Fail: Test 2 failed'
    assert len(get_unique_ways1(3)) == 3, 'Fail: Test 3 failed'
    assert len(get_unique_ways1(4)) == 5, 'Fail: Test 4 failed'
    assert len(get_unique_ways1(5)) == 8, 'Fail: Test 5 failed'

    n = int(input("Enter the number of steps\n"))
    result = get_unique_ways1(n)
    print("Number of ways to climb {} steps, being able to climb [1,2] steps at a time, is: {}".format(n, len(result)))
    print("Unique ways: ", result)

    # With steps = {ANYTHING}
    assert len(get_unique_ways2(5, [1, 2])) == 8, 'Fail: Test 6 failed'
    assert len(get_unique_ways2(5, [1, 3])) == 4, 'Fail: Test 7 failed'
    assert len(get_unique_ways2(7, [2, 3, 4])) == 5, 'Fail: Test 7 failed'

    n = int(input("Enter the number of steps\n"))
    steps_in = input("Enter a list of steps that can be climbed, separated by space\n").split()
    steps = np.sort(np.asarray(steps_in, dtype=np.int))
    steps = np.array([s for s in steps if s <= n])

    result = get_unique_ways2(n, steps)
    print("Number of ways to climb {} steps, being able to climb {} steps at a time, is: {}".format(n, steps_in, len(result)))
    print("Unique ways: ", result)
