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
    # Use the index itself to check the number exists or not
    # First sort the array with one pass O(N) keeping all non-postive integers ar the end
    arr_size = len(arr)
    for i in range(arr_size):
        while 0 < arr[i] < arr_size:
            val = arr[i]
            arr[i], arr[val - 1] = arr[val - 1], arr[i]
            if arr[i] == arr[val - 1]:
                break

    # Iterate the array and return the first index that breaks the continuity
    for i, item in enumerate(arr):
        if item != i + 1:
            return i + 1

    return arr_size + 1


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)

    result = find_missing_number(in_list)
    print("Missing number from the given list is: ", result)