"""
return a new sorted merged list from K sorted lists, each with size N

Note: This is the solution given by Daily Coding Problems. (https://www.dailycodingproblem.com/)
      It is neither my solution nor I own this solution
"""

import os
import sys
import numpy as np
import heapq


def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list


if __name__ == '__main__':
    assert merge([]) == [], "Error! Test-1 failed"
    assert merge([[], [], []]) == [], "Error! Test-2 failed"
    assert merge([[], [1], [1, 2]]) == [1, 1, 2], "Error! Test-3 failed"
    assert merge([[1]]) == [1], "Error! Test-4 failed"
    assert merge([[1], [1, 3, 5], [1, 10, 20, 30, 40]]) == [1, 1, 1, 3, 5, 10, 20, 30, 40], "Error! Test-5 failed"

    print("All 5 tests passed")
