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

    if len(arr) == 1:
        print("Max(", arr, ") = ", arr[0])
        return

    if len(arr) == 2:
        if k == 1:
            print("Max(", arr[0], ") = ", arr[0])
            print("Max(", arr[1], ") = ", arr[1])
        else:
            print("Max(", arr, ") = ", max(arr))
        return

    max_idx = -1
    next_max_idx = -1

    for i, element in enumerate(arr):
        if i == 0:
            max_idx = i
        elif i == 1:
            max_idx = i if element > arr[max_idx] else max_idx
            next_max_idx = 1 if element < arr[max_idx] else 0
        elif i < k:
            if arr[max_idx] < element:
                max_idx = i
            elif (element > arr[next_max_idx]) and (element < arr[max_idx]):
                next_max_idx = i

            if i == k-1:
                print("Max(", arr[i-k+1:i+1], ") = ", arr[max_idx])
        else:
            if max_idx == i-k:
                if element > arr[next_max_idx]:
                    max_idx = i
                else:
                    max_idx = next_max_idx
            else:
                max_idx = i if element > arr[max_idx] else max_idx
                next_max_idx = i if (element > arr[next_max_idx]) and (element < arr[max_idx]) else next_max_idx

            print("Max(", arr[i-k+1:i+1], ") = ", arr[max_idx])





if __name__ == '__main__':
    # Given test case
    print("------------------------Given case------------------------")
    arr = [10, 5, 2, 7, 8, 7]
    print("Input array is: ", arr, " with k: ", 3)
    max_subarray(arr, k=3)

    # Increasing test case
    print("\n------------------------Increasing case------------------------")
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Input array is: ", arr, " with k: ", 4)
    max_subarray(arr, k=4)

    # Increasing test case
    print("\n------------------------Decreasing case------------------------")
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print("Input array is: ", arr, " with k: ", 4)
    max_subarray(arr, k=4)

    # Random case
    print("\n------------------------Random case------------------------")
    arr = np.random.randint(low=0, high=10, size=10)
    print("Input array is: ", arr, " with k: ", 3)
    max_subarray(arr, k=3)
