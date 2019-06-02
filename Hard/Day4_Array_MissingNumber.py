"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

import os
import sys
import numpy as np


def find_missing_number(arr):
    pass


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)

    result = find_missing_number(in_list)
    print("Missing number from the given list is: ", result)