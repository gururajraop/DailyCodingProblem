"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

Implement car and cdr.
"""

import os
import sys
import numpy as np
import random


# Given Python Closure
# More on python closures: https://en.wikipedia.org/wiki/Closure_(computer_programming)
# and https://www.programiz.com/python-programming/closure
# and https://www.learnpython.org/en/Closures
def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# Return the first element of the pair
def car(pair):
    # return pair.__closure__[0].cell_contents   # Not very best solution
    return pair(lambda a, b: a)


# Return the last element of the pair
def cdr(pair):
    # return pair.__closure__[1].cell_contents    # Not very best solution
    return pair(lambda a, b: b)


if __name__ == '__main__':
    a = random.randrange(10)
    b = random.randrange(10)
    print("Given pair of integers are ({}, {})".format(a, b))
    assert car(cons(a, b)) == a, "Failure: Test 1 (first element extraction) failed"
    assert cdr(cons(a, b)) == b, "Failure: Test 2 (last element extraction) failed"
    print("PASS")
