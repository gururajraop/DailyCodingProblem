"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

import os
import sys
import numpy as np


def simple_logic(a, k):
    result = {}
    a = np.unique(a)
    key = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]+a[j] == k:
                result[key] = (a[i], a[j])
                key += 1

            if a[j] >= k:
                break
        if a[i] >= k:
            break

    return result


def single_pass(a, k):
    result = {}
    a = np.unique(a)
    key = 0
    sum = a[a < k]
    for i in range(len(sum)):
        new_sum = sum[i] + sum[i+1:]
        if any(new_sum == k):
            indices = np.where(new_sum == k)[0]
            result[key] = (sum[i], sum[indices+i+1][0])
            key += 1

        if sum[i] >= k:
            break

    return result


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)
    k = int(input("Enter the value of k:\t"))

    print("--------------------------Simple Logic--------------------------")
    result = simple_logic(in_list, k)
    if len(result) > 0:
        print("The list contains elements adding up to {}".format(k))
        print(result.values())
    else:
        print("The list doesn't contain elements adding up to {}".format(k))

    print("--------------------------Single Pass--------------------------")
    result = single_pass(in_list, k)
    if len(result) > 0:
        print("The list contains elements adding up to {}".format(k))
        print(result.values())
    else:
        print("The list doesn't contain elements adding up to {}".format(k))