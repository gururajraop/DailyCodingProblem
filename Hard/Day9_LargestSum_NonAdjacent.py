"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
Similarly, [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

import os
import sys
import numpy as np


def simple_logic(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return max(arr[0], arr[1])

    sum1 = arr[0] + simple_logic(arr[2:])
    sum2 = arr[1] + simple_logic(arr[3:])

    return max(sum1, sum2)


def one_pass(arr):
    return 0


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)

    print("--------------------------Simple Logic--------------------------")
    result = simple_logic(in_list)
    print("The largest sum of non-adjacent numbers is: ", result)

    print("--------------------------Single  Pass--------------------------")
    result = one_pass(in_list)
    print("The largest sum of non-adjacent numbers is: ", result)