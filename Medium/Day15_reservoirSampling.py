"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

import os
import sys
import numpy as np
import random


def reservoirSampling(arr):
    items = []

    for i, e in enumerate(arr):
        if random.randint(1, i + 1) == 1:
            items.append(e)

    return items


if __name__ == '__main__':
    n = int(input("Enter the size of the array: "))
    arr = np.random.randint(low=0, high=100, size=n)
    item = reservoirSampling(arr)
    print("Randomly sampled items from the array are: ", item)