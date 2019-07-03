"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""

import os
import sys
import numpy as np


def max_subarray(arr, k):
    assert (0 < k) and (k <= len(arr)), "Invalid value of k"

    max_idx = 0
    next_max_idx = 0
    indices = []
    for i, element in enumerate(arr):
        if i < k:
            if arr[max_idx] < element:
                max_idx = i
            if (element > arr[next_max_idx]) and (element < arr[max_idx]):
                next_max_idx = i
            indices.append(i)
            if i == k-1:
                print("Max(", arr[i-k+1:i+1], ") = ", arr[max_idx])
        else:
            if max_idx == i-k:
                max_idx = i if element > arr[next_max_idx] else i
            else:
                max_idx = i if element > arr[max_idx] else max_idx
                next_max_idx = i if (element > arr[next_max_idx]) and (element < arr[max_idx]) else next_max_idx

            print("Max(", arr[i-k+1:i+1], ") = ", arr[max_idx])





if __name__ == '__main__':
    # Given test case
    arr = [10, 5, 2, 7, 8, 7]
    max_subarray(arr, k=3)

    # Random case
    #arr = np.random.randint(low=0, high=10, size=10)
    #print("Input array is: ", arr)
    #max_subarray(arr, k=3)
