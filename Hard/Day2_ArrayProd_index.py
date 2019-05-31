"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

import os
import sys
import numpy as np


def simple_logic(arr):
    total_prod = np.prod(arr)
    new_arr = [total_prod / element for element in arr]

    return new_arr


def no_division(arr):
    new_arr = np.ones(len(arr))
    indices = np.arange(len(arr))
    for i, element in enumerate(arr):
        new_arr[i] = np.prod(arr[np.where(indices != i)])

    return new_arr


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)

    print("--------------------------Simple Logic--------------------------")
    result = simple_logic(in_list)
    print("The new array is: ", result)

    print("--------------------------No division--------------------------")
    result = no_division(in_list)
    print("The new array is: ", result)