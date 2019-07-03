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
from collections import deque


def max_subarray(arr, k):
    assert (0 < k) and (k <= len(arr)), "Invalid value of k"

    # Just return the single element from the array
    if len(arr) == 1:
        print("Max(", arr, ") = ", arr[0])
        return

    # Return the max of the 2 elements
    if len(arr) == 2:
        if k == 1:
            print("Max(", arr[0], ") = ", arr[0])
            print("Max(", arr[1], ") = ", arr[1])
        else:
            print("Max(", arr, ") = ", max(arr))
        return

    # Use double ended queue to sort the max items
    double_ended_queue = deque()
    for i, element in enumerate(arr):
        # Untill the queue fills in, just append the items
        if i < k:
            while double_ended_queue:
                # If the current item bigger than previous,
                # remove all the previous items
                if element >= arr[double_ended_queue[-1]]:
                    double_ended_queue.pop()
                else:
                    break
            # Add the current index
            double_ended_queue.append(i)
            if i == k-1:
                print("Max(", arr[i-k+1:i+1], ") = ", arr[double_ended_queue[0]])
        else:
            # Remove the item from the front if that is the max
            if double_ended_queue[0] <= i-k:
                double_ended_queue.popleft()

            # If the current item is bigger than previous
            # remove all such items from the queue
            while double_ended_queue:
                if element >= arr[double_ended_queue[-1]]:
                    double_ended_queue.pop()
                else:
                    break

            # Append the current index
            double_ended_queue.append(i)

            print("Max(", arr[i-k+1:i+1], ") = ", arr[double_ended_queue[0]])


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
