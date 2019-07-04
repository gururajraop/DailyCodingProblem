"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
"""

import os
import sys
import numpy as np


def find_min_cost(cost_matrix):
    return 0


if __name__ == '__main__':
    N = np.random.randint(low=5, high=10, size=1)[0]
    K = np.random.randint(low=2, high=N, size=1)[0]
    cost_matrix = np.random.randint(low=30, high=100, size=(N, K))

    min_cost = find_min_cost(cost_matrix)
    print("Total cost of coloring {} houses with {} colors is {}".format(N, K, min_cost))