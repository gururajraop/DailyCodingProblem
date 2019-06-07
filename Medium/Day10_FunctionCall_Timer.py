"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import os
import sys
import numpy as np
import time


def f():
    print("Inside function f()")


if __name__ == '__main__':
    call_time = int(input("Enter the time in ms after which function f to be called: "))
    start = time.time()
    while True:
        dur = int((time.time() - start) * 1000)
        if dur >= call_time:
            print("Calling function f() after {} ms".format(dur))
            f()
            break