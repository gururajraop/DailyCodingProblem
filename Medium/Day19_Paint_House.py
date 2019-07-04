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
    N, K = cost_matrix.shape
    solution = list(np.zeros((1, K)))

    for h, house in enumerate(cost_matrix):
        house_cost = []
        for c, cost in enumerate(house):
            min_cost = min([solution[h][i] for i in range(K) if i != c])
            house_cost.append(min_cost + cost)
        solution.append(house_cost)

    min_cost = min(solution[-1])

    return min_cost


if __name__ == '__main__':
    cost_matrix = np.array([[11, 47], [18, 37], [24, 40]])
    min_cost = find_min_cost(cost_matrix)
    print("Total cost of coloring {} houses with {} colors is {}".format(3, 2, min_cost))


    N = np.random.randint(low=5, high=10, size=1)[0]
    K = np.random.randint(low=2, high=N, size=1)[0]
    cost_matrix = np.random.randint(low=30, high=100, size=(N, K))

    min_cost = find_min_cost(cost_matrix)
    print("Total cost of coloring {} houses with {} colors is {}".format(N, K, min_cost))