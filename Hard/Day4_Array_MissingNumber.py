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


def get_positive_subarray(arr):
    """Get the subarray with positive elements only"""
    sub_array = []
    for item in arr:
        if item > 0:
            sub_array.append(item)

    return np.array(sub_array)


def find_missing_number(arr):
    pos_arr = get_positive_subarray(arr)
    arr_size = len(pos_arr)

    # Set all the numbers in the linear space to negative constant space
    # if the index falls in the linear positive constance space
    for num in pos_arr:
        index = abs(num) - 1
        # Change the number to negative space iff
        # 1: The index should be valid ie between 0 and size of positive array
        # 2: The number at position shouldn't be changed already due to duplicate elements
        if (index >= 0) and (index < arr_size) and pos_arr[index] > 0:
            pos_arr[index] *= -1

    # return the first item in the positive list that didn't change to negative space
    for i in range(arr_size):
        if pos_arr[i] > 0:
            return i+1

    # return the number next in the linear space
    return arr_size + 1


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)

    result = find_missing_number(in_list)
    print("Missing number from the given list is: ", result)