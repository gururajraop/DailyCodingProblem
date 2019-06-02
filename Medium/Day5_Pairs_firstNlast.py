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


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# Return the first element of the pair
def car(pair):
    pass


# Return the last element of the pair
def car(pair):
    pass


if __name__ == '__main__':
    a = random.randrange(10)
    b = random.randrange(10)
    assert car(cons(a, b)) == b, "Failure: Test 1 (first element extraction) failed"
    assert cdr(cons(a, b)) == b, "Failure: Test 2 (last element extraction) failed"
    print("PASS")
