"""
The area of a circle is defined as pi*r*r. Estimate pi to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

import os
import sys
import numpy as np
import random


def compute_pi(n):
    count = 0
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance < 1:
            count = count + 1

    pi_val = (count / n) * 4
    return pi_val


if __name__ == '__main__':
    n = int(input("Enter the number of samples for the Monte Carlo method: "))
    print("Computed value of pi={0:.6f}".format(compute_pi(n)))