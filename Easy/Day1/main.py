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

    return result


def single_pass(a, k):
    pass


if __name__ == '__main__':
    input_string = input("Enter a list of numbers separated by space\n")
    in_list = input_string.split()
    in_list = np.asarray(in_list, dtype=np.int)
    k = int(input("Enter the value of k:\t"))

    result = simple_logic(in_list, k)
    if len(result) > 0:
        print("The list contains elements adding up to {}".format(k))
        print(result.values())
    else:
        print("The list doesn't contain elements adding up to {}".format(k))

    #result = single_pass(in_list, k)
    #print(result)